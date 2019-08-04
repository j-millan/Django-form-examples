from django.db import models
from django_countries import fields as country_fields
from phonenumber_field import modelfields as phonenumber_fields

class JobApplication(models.Model):
	name = models.CharField(max_length=35)
	last_name = models.CharField(max_length=35)
	birth_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	sex_list = (('M', 'Male'), ('F', 'Female'))
	sex = models.CharField(max_length=1, choices=sex_list)
	country = country_fields.CountryField()
	phone_number = phonenumber_fields.PhoneNumberField()
	about = models.CharField(max_length=250)

	def __str__(self):
		return "{0} {1}".format(self.name, self.last_name)

class Car(models.Model):
	brand_list = (
		('TY', 'Toyota'),
		('CH', 'Chevrolet'),
		('FD', 'Ford')
	)

	color_list = (
		('RD', 'Red'),
		('BL', 'Blue'),
		('GR', 'Green'),
		('PR', 'Purple'),
		('BK', 'Black'),
		('YW', 'Yellow'),
		('BW', 'Brown'),
		('WH', 'White')
	)

	brand = models.CharField(max_length=2, choices=brand_list)
	color = models.CharField(max_length=2, choices=color_list)
	fuel_capacity = models.IntegerField()
	leather_seats = models.BooleanField(default=False)
	dark_windows = models.BooleanField(default=True)

	def __str__(self):
		return '{0} number: '.format(self.brand, self.pk)