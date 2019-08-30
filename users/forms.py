from django import forms
from users.models import *

class SignInForm(forms.ModelForm):
	email = forms.EmailField(max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email Address'} ))
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'} ))
	
	class Meta:
		model = User
		fields = ('email', 'password')


class SignUpForm(forms.ModelForm):
	email = forms.EmailField(max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email Address'} ))
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'} ))
	
	class Meta:
		model = User
		fields = ('email', 'password')


class ResetPasswordForm(forms.ModelForm):
	email = forms.EmailField(max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email Address'} ))
	
	class Meta:
		model = User
		fields = ('email',)


class VerifyPasswordResetCode(forms.Form):
	code = forms.CharField(max_length = 6, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Unique Code'} ))


class NewPassword(forms.Form):
	password = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'New Password'} ))