from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# emailing stuff
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from .utils import token_generator

def home_page(request):
    return render(request, 'register/home.html')

def register(request):
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()

            # encoding user id to send over the network

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('register:activate', kwargs={'uidb64':uidb64, 'token':token_generator.make_token(user)})

            activate_url = 'http://'+domain+link

            email_subject = 'Activate your account'
            email_body = 'Hi '+user.username+' Please use this link to verify your account.\n'+activate_url

            email = EmailMessage(
                email_subject,
                email_body,
                'testexpenses724@gmail.com',
                [user.email],
                )

            email.send(fail_silently=False)
            messages.success(request, 'Account successfully created. Please check your email for the verification link')

            return redirect('register:login')
            # return redirect(reverse('mainapp:home_page'))
        else:
            return render(request, 'register/register.html', {'user_form': user_form})

    else:
        user_form = forms.UserForm()

    return render(request, 'register/register.html', {'user_form': user_form})

def user_verify(request, uidb64, token):

    # verifying the user have the correct link and avtivating the user

    if request.method == 'GET':
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('register')

            if user.is_active:
                return redirect('register:login')

            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('register:login')

        except Exception as e:
            pass

        return redirect('register:login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'mainapp/home.html', {'message': 'Logged in successfully!'})
        else:
            messages.warning(request, 'You need to register yourself first!')
            return redirect('/register/')
    else:
        return render(request, 'register/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('mainapp:home_page'))
