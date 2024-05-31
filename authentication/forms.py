# forms.py
from django import forms
from django.contrib.auth.models import User  


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['username'].label = 'User Name'
        self.fields['username'].help_text = None

        
    

class LoginForm(forms.Form):
    uname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)