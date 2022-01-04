# from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# emailing stuff
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from .utils import token_generator, forgot_password_token

def home_page(request):
    return render(request, 'register/home.html')



def register(request):
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            password1 = user_form.cleaned_data.get('password1')
            user.last_name=request.POST['lname']
            user.first_name=request.POST['fname']
            user.set_password(password1)
            user.is_active = False
            user.save()
            # encoding user id to send over the network

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            # Use the code below to get domain name
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
        else:
            return render(request, 'register/register.html', {'user_form': user_form, 'errors':user_form.errors})

    else:
        user_form = forms.UserForm()

    return render(request, 'register/register.html', {'user_form': user_form, 'errors':user_form.errors})

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
    if request.user.is_authenticated:
        messages.success(request, 'Logged in successfully!')
        return render(request, 'mainapp/home.html', {'message': 'Logged in successfully!'})
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return render(request,  'mainapp/home.html', {'message': 'Logged in successfully!'})
            else:
                messages.warning(request, 'You have not activated your account, activate using the link sent to your mail.')
                return render(request, 'register/login.html', {'error': 'You have not activated your account, activate using the link sent to your mail.'})
        else:
            try:
                user=User.objects.get(username=username)
                if not user.is_active:
                    messages.warning(request, 'You have not activated your account, activate using the link sent to your mail.')
                    return render(request, 'register/login.html', {'error': 'You have not activated your account, activate using the link sent to your mail.'})
                if not user.check_password(password):
                    messages.warning(request, 'Incorrect Password')
                    return render(request, 'register/login.html', {'error':'Incorrect Password'})
            except:
                messages.warning(request, 'You need to register yourself first!')
                return redirect('/register/')
    else:
        return render(request, "register/login.html")

def forgot_password(request):
    User=get_user_model()
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        try:
            user=User.objects.get(username=username)
            if password1==password2:
                user.set_password(password1)
                user.save()
                messages.success(request, 'Password has been reset successfully!')
                return redirect('register:login')
            else:
                messages.warning(request, 'Passwords do not match')
                return redirect('register:forgot_password')
        except User.DoesNotExist:
            messages.warning(request,'No user found with username: '+username)
            return redirect('register:forgot_password')
    else:
        return render(request,'register/forgot_password.html')




@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('mainapp:home_page'))

