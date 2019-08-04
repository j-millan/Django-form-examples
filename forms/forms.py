from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from . import models

class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		max_length=130, 
		required=True, 
		widget=forms.EmailInput()
	)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CarForm(forms.ModelForm):
	class Meta:
		model = models.Car
		fields = ['brand', 'color', 'fuel_capacity', 'leather_seats', 'dark_windows']

class JobApplicationForm(forms.ModelForm):
	birth_date = forms.DateField(widget=forms.SelectDateWidget(
		empty_label=['Choose year', 'Choose month', 'Choose day'],
		years=range(1975, 2010)
	))

	phone_number = PhoneNumberField()
	
	class Meta:
		model = models.JobApplication
		fields = ['name', 'last_name', 'birth_date', 'country', 'phone_number']
