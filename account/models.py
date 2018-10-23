from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=400, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	location = models.CharField(max_length=100, default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to='profile_image', blank=True)
	
	

	def __str__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)		


