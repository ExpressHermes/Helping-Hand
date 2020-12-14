from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta():
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'true'
        })
