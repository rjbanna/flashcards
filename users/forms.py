from django import forms
from users.models import *
from carddecks.models import *

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


# class DeckAddForm(forms.Form):
# 	name = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Deck Name'} ))
# 	user = forms.CharField(max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Deck Name'} ))


# 	def save(self):
# 	    data = self.cleaned_data
# 	    user = Deck(user = request.session['email'], name = data['name'])
# 	    user.save()


class DeckAddForm(forms.ModelForm):
	name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Deck Name'} ))

	class Meta:
		model = Deck
		fields = ('name',)


class CardAddForm(forms.Form):
	front = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Card Front'} ))
	back = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Card Back'} ))
	decks = forms.ModelChoiceField(queryset = Deck.objects.all().order_by('name'))

	def save(self):
	    data = self.cleaned_data
	    user = Card(deck_name = data['decks'], front = data['front'], back = data['back'])
	    user.save()

	# class Meta:
	# 	model = Card
	# 	fields = ('front', 'back', 'decks')