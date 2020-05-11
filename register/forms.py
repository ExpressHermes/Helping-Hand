from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
