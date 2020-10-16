from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm,UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from .models import Post


class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class': 'form-control'}),
        'first_name':forms.TextInput(attrs={'class': 'form-control'}),
        'last_name':forms.TextInput(attrs={'class': 'form-control'}),
        'email':forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UpdateSignUpForm(UserChangeForm):
    class Meta:
        model = User
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        fields = ['first_name', 'last_name', 'email']
        widgets = {'first_name':forms.TextInput(attrs={'class': 'form-control'}),
        'last_name':forms.TextInput(attrs={'class': 'form-control'}),
        'email':forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title':'Title', 'content': 'Blog Content'}
        widgets = {'title':forms.TextInput(attrs={'class': 'form-control'}),
        'content':forms.Textarea(attrs={'class': 'form-control'})
        }
