# # from django import forms
# # from django.contrib.auth.models import User

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# #from .models import CustomUser
# from django.contrib.auth.models import User
# from .models import *

# class UserForm(UserCreationForm):
#     #password = forms.CharField(widget=forms.widgets.PasswordInput)
#     email = forms.EmailField(required=True)

#     class Meta():
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     for field in iter(self.fields):
#     #         self.fields[field].widget.attrs.update({
#     #             'class': 'form-control'
#     #     })
#     # class Meta:
#     #     model = User
#     #     fields = ("username", "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(UserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

# from django import forms
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
 
# from .models import * 
 
# class UserForm(forms.ModelForm):
#    password = forms.CharField(label='Password', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#    email = forms.EmailField(required=True)    

#    class Meta:
#        model = User
#        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')
 
#    def clean_password2(self):
#        # Check that the two password entries match
#        password = self.cleaned_data.get("password")
#        password2 = self.cleaned_data.get("password2")
#        if password and password2 and password != password2:
#            raise ValidationError("Passwords don't match")
#        return password2
 
#    def save(self, commit=True):
#        # Save the provided password in hashed format
#        user = super().save(commit=False)
#        user.set_password(self.cleaned_data["password"])
#        if commit:
#            user.save()
#        return user

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username",'first_name', 'last_name', "email", "password1", "password2")

    
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })