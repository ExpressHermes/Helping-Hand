from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    return render(request, 'register/home.html')

def register(request):
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect(reverse('register:home_page'))
        else:
            return render(request, 'register/register.html', {'user_form': user_form})

    else:
        user_form = forms.UserForm()

    return render(request, 'register/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'register/home.html', {'message': 'Logged in successfully!'})
        else:
            return render(request, 'register/home.html', {'message': 'You need to register yourself first'})
    else:
        return render(request, 'register/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('register:home_page'))
