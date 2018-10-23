from django.db import models

# Create your models here.

class CustomerEmail(models.Model):
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.email

class CustomerNumber(models.Model):
	to_number = models.IntegerField(default=0)

	def __int__(self):
		return self.to_number		