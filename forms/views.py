from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CarForm, JobApplicationForm, SignUpForm
from .models import Car, JobApplication

def user_home(request):
	return render(request, 'forms/auth/user_home.html')

def sign_up(request):
	form = None
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('forms:user_home')

	else:
		form = SignUpForm()

	return render(request, 'forms/auth/sign_up.html', {'form' : form})

def job_application(request):
	form = None
	if request.method == "POST":
		form = JobApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('forms:job_app')

	else:
		form = JobApplicationForm()

	return render(request, 'forms/job_application.html', {'form' : form})

def new_car(request):
	form = None
	if request.method == "POST":
		form = CarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('forms:new_car')

	else:
		form = CarForm()

	return render(request, 'forms/new_car.html', {'form' : form})