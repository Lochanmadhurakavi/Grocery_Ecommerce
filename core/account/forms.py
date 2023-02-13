from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs=
                                {
                                    'placeholder':'Enter the username',
                                    'class':'form-control'
                                }))
    password = forms.CharField(widget=forms.TextInput(attrs={
                                'placeholder':'Enter the password',
                                'class':'form-control'
    }))


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Enter the username',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class':'form-control',
                            'placeholder':'Enter your email',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                            'class':'form-control',
                            'placeholder':'Enter your password',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                            'class':'form-control',
                            'placeholder':'Enter your password again',
    }))