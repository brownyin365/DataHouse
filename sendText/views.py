from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import sendgrid
import os
from sendgrid.helpers.mail import *
from django.conf import settings
from .models import CustomerEmail, CustomerNumber
import nexmo
from django.core.mail import send_mail, BadHeaderError



# Create your views here.

def index(request):	
	return render(request, 'index.html', {})


def select(request):
	return render(request, 'select.html', {})


def send_sms(request):
	return render(request, 'sendsms/send_sms.html', {})

def sms_success(request):
	client = nexmo.Client(key=settings.NEXMO_API_KEY, secret=settings.NEXMO_API_SECRET)
	to_number = request.POST.get("to_number", ''),
	message = request.POST.get("message"),
	# user = CustomerNumber(to_number=to_number)
	# user.save()
	client.send_message({
	    'from': '365ServersGH',
	    'to': to_number,
	    'text': message,
		})
	return render(request, 'sendsms/sms_success.html', {})	




def send_email(request):
    return render(request, 'sendemail/send_email.html', {})

def success(request):
	email = request.POST.get('email', '')
	data = """
	Hello there!

	I wanted to personally write an email in order to welcome you to our platform.\
	 We have worked day and night to ensure that you get the best service. I hope \
	that you will continue to use our service. We send out a newsletter once a \
	week. Make sure that you read it. It is usually very informative.GHANA

	Cheers!
	~ 365ServersGH
    """
	user = CustomerEmail(email=email)
	user.save()
	send_mail('Welcome', 
			data, 
			'365serversgh', 
			[email], 
			fail_silently=False)
	return render(request, 'sendemail/success.html', {})







