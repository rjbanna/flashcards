from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import *
from django.contrib import messages
import uuid
from django.conf import settings

# Create your views here.

def homepage(request):
	return redirect('signin')

# ---------------------------------------- BEFORE LOGIN FUNCTIONS START ---------------------------------------- #
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
				return redirect('dashboard')
		else:
			return render(request, template_name = 'signup.html', context = { 'form': form })

	else:
		form = SignUpForm()

	return render(request, template_name = 'signup.html', context = { 'form': form })

def resetpass(request):
	if 'email' in request.session:
		return redirect('dashboard')

	if request.method == 'POST':
		form = ResetPasswordForm(request.POST)

		email = request.POST['email']
		check_email = User.objects.filter(email = email)

		if check_email:
			try:
				unique_id = uuid.uuid1()
				user_data = User.objects.get(email = email)
				user_data.activation_code = unique_id
				user_data.save()
				subject = "So sad!"
				message = 'Here\'s the secret code to reset your password \n' + str(unique_id)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email]
				send_mail(subject, message, from_email, to_list, fail_silently = False)
			except:
				return False
				
			return redirect('signin')
		else:
			message.error(request, 'Email is not registered' )
			return redirect('resetpass')
	else:
		form = ResetPasswordForm()

	return render(request, template_name = 'signup.html', context = { 'form': form })


def verify_email(request):
	pass
# ---------------------------------------- BEFORE LOGIN FUNCTIONS STOP ---------------------------------------- #



# ---------------------------------------- AFTER LOGIN FUNCTIONS START ---------------------------------------- #
def dashboard(request):
	if 'email' not in request.session:
		return redirect('signin')

	return render(request, template_name = 'dashboard.html', context = { 'form': 'aa' })

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
				request.session['email'] = email
				return redirect('dashboard')
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
# ---------------------------------------- AFTER LOGIN FUNCTIONS STOP ---------------------------------------- #