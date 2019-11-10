from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CarForm, JobApplicationForm, SignUpForm, ProtectorForm
from .models import Protector

def user_home(request):
	return render(request, 'forms/auth/logout_request.html')

def logout_request(request):
	if request.user.is_authenticated:
		return render(request, 'forms/auth/logout_request.html')
	else:
		return  redirect('forms:login')

def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('forms:user_home')

	else:
		if request.user.is_authenticated:
			return redirect('forms:logout_request')

		form = SignUpForm()

	return render(request, 'forms/auth/sign_up.html', {'form' : form})

def job_application(request):
	if request.method == "POST":
		form = JobApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('forms:job_app')

	else:
		form = JobApplicationForm()

	return render(request, 'forms/job_application.html', {'form' : form})

def new_car(request):
	if request.method == "POST":
		form = CarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('forms:new_car')

	else:
		form = CarForm()

	return render(request, 'forms/new_car.html', {'form' : form})

def protector_registration(request):
	if request.method == "POST":
		form = ProtectorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('forms:protect')

	else:
		form = ProtectorForm()

	return render(request, 'forms/protector_registration.html', {'form' : form, 'protectors' : Protector.objects.all})