from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import *
from django.contrib import messages
from django.core.mail import send_mail
import uuid
from django.conf import settings
from random import randint
from django.urls import reverse

from carddecks.models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def homepage(request):
	return redirect('signin')



# ---------------------------------------- BEFORE LOGIN FUNCTIONS START --------------------------------------- #
def signup(request):
	if 'email' in request.session:
		return redirect('dashboard')
		
	if request.method == 'POST':		
		email = request.POST['email']
		password = request.POST['password']

		email_unique = User.objects.filter(email = email)

		if email_unique.count() > 0:
			messages.error(request, "Email already registered");

		if not len(password) >= 8:
			messages.error(request, "Password must be 8 characters long");

		form = SignUpForm(request.POST)
		if len(messages.get_messages(request)) == 0:
			if form.is_valid():
				user = form.save(commit = False)
				user.save()
				activation_mail(request, email)
		else:
			messages.error(request, "Solve errors")
			return render(request, template_name = 'signup.html', context = { 'form': form })

	else:
		form = SignUpForm()

	return render(request, template_name = 'signup.html', context = { 'form': form })

def activation_mail(request, email):
	try:
		unique_id = unique_code(6)
		email_active_url = request.META['HTTP_HOST'] + reverse('account_active') + '?q=' + str(unique_id)

		user_data = User.objects.get(email = email)
		user_data.activation_code = unique_id
		user_data.save()

		subject = "Welcome to Flashyy"
		message = 'Please click on this link to activate your account \n' + email_active_url
		from_email = settings.EMAIL_HOST_USER
		to_list = [email]
		
		send_mail(subject, message, from_email, to_list, fail_silently = False)
		messages.success(request, 'Account activation mail sent')
		return redirect('signin')		
	except:
		return False

def account_active(request):
    try:
        unique_id = request.GET['q']
        customer_data = User.objects.filter(activation_code = unique_id)

        if(customer_data.count() > 0):
            messages.success(request, 'Your account has been activated please Log in below')
            customer_data = User.objects.get(activation_code = unique_id)
            customer_data.activation_code = ''
            customer_data.is_active = 1
            customer_data.save()

            return redirect('signin')
        else:
            messages.error(request, 'Invalid URL')
            return redirect('signin')
    except:
        return redirect('signin')
# ---------------------------------------- BEFORE LOGIN FUNCTIONS STOP ---------------------------------------- #



# ---------------------------------------- AFTER LOGIN FUNCTIONS START ---------------------------------------- #
def dashboard(request):
	if 'email' not in request.session:
		return redirect('signin')

	email = request.session['email']
	user_decks_check = Deck.objects.filter(user__email = email)

	is_created = 0
	get_user_decks = []
	if user_decks_check:
		for d in user_decks_check:
			get_user_decks.append(d)

		is_created = 1

	return render(request, template_name = 'dashboard.html', context = { 'is_created': is_created, 'decks': get_user_decks })

def signin(request):
	if 'email' in request.session:
		return redirect('dashboard')

	if request.method == 'POST':		
		email = request.POST['email']
		password = request.POST['password']

		check_user = User.objects.filter(email = email, password = password)

		form = SignInForm(request.POST)

		if check_user:
			if form.is_valid():
				user_data = User.objects.get(email = email)

				if user_data.is_active:
					request.session['email'] = email
					return redirect('dashboard')
				else:
					request.session['send_again_mail'] = email
					messages.info(request, 'Please activate your account to continue login')
					return render(request, template_name = 'signin.html', context = {'form': form, 'send_mail': 1})
		else:
			messages.error(request, 'Please check your email / password')
			return redirect('signin')
	else:
		form = SignInForm()

	return render(request, template_name = 'signin.html', context = {'form': form})

def signout(request):
	if 'email' not in request.session:
		return redirect('homepage')

	request.session.flush()
	return redirect('homepage')
# ---------------------------------------- AFTER LOGIN FUNCTIONS STOP ----------------------------------------- #



# -------------------------------------- PASSWORD RELATED FUNCTIONS START ------------------------------------- #
def resetpass(request):
	if 'email' in request.session:
		return redirect('dashboard')

	if request.method == 'POST':
		form = ResetPasswordForm(request.POST)

		if form.is_valid():
			email = request.POST['email']
			check_email = User.objects.filter(email = email)

			if check_email:
				# unique_id = uuid.uuid1()
				unique_id = unique_code(6)
				user_data = User.objects.get(email = email)
				user_data.password_reset_code = unique_id
				user_data.save()

				subject = "So sad!"
				message = 'Here\'s the secret code to reset your password \n' + str(unique_id)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]
				
				send_mail(subject, message, from_email, to_list, fail_silently = False)			
				
				request.session['temp_mail'] = email

				return redirect('resetpassverify')
			else:
				messages.error(request, 'Email is not registered' )
				return redirect('resetpass')
		else:
			messages.error(request, 'Error occured' )
			return redirect('resetpass')
	else:
		form = ResetPasswordForm()

	return render(request, template_name = 'password/resetpassword.html', context = { 'form': form })

def verify(request):
	if 'email' in request.session:
		return redirect('dashboard')

	if 'temp_mail' not in request.session:
		return redirect('homepage')

	if request.method == 'POST':
		email = request.session['temp_mail']
		code = request.POST['code']

		form = VerifyPasswordResetCode(request.POST)

		if form.is_valid():
			user_account = User.objects.filter(email = email)

			if user_account:			
				user_data = User.objects.get(email = email)

				if user_data.password_reset_code == code:
					user_data.password_reset_code = ''
					user_data.save()
					request.session['is_verified'] = 1
					return redirect('newpassword')
				else:
					messages.error(request, 'Wrong unique code')
				
				return redirect('resetpassverify')
			else:
				messages.error(request, 'Wrong unique code')
				return redirect('resetpassverify')
		else:
			return redirect('resetpassverify')

	else:
		form = VerifyPasswordResetCode()

	return render(request, template_name = 'password/verifycode.html', context = {'form': form})

def newpassword(request):
	if 'email' in request.session:
		return redirect('dashboard')

	if 'temp_mail' not in request.session:
		return redirect('homepage')

	if 'is_verified' not in request.session:
		return redirect('homepage')

	if request.method == 'POST':
		email = request.session['temp_mail']
		password = request.POST['password']

		form = NewPassword(request.POST)

		if form.is_valid():
			user_account = User.objects.filter(email = email)

			if user_account:
				user_data = User.objects.get(email = email)
				user_data.password = password
				user_data.save()

				del request.session['temp_mail']
				del request.session['is_verified']

				messages.success(request, 'Password changed successfully')
				return redirect('signin')
			else:
				messages.error(request, 'Error occured')
				return redirect('newpassword')
		else:
			return redirect('newpassword')

	else:
		form = NewPassword()

	return render(request, template_name = 'password/newpassword.html', context = {'form': form})

def unique_code(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
# --------------------------------------- PASSWORD RELATED FUNCTIONS STOP ------------------------------------- #



# ------------------------------------------------ OTHERS START ----------------------------------------------- #
def send_activation_mail_again(request):
	email = request.session['send_again_mail']
	activation_mail(request, email)
	del request.session['send_again_mail']
	return redirect('signin')
# ------------------------------------------------ OTHERS STOP ------------------------------------------------ #



def deck_detail(request, slug = True):
	if 'email' not in request.session:
		return redirect('signin')

	deck = get_object_or_404(Deck, slug = slug)
	return render(request, template_name = 'carddecks/deck_details.html', context = {'deck': deck})
