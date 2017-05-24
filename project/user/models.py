from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# class User(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	username = models.CharField(max_length=15)
# 	password = models.CharField(max_length=20)
# 	first_name = models.TextField()
# 	last_name = models.TextField()
# 	create_date = models.DateTimeField()

# 	def __str__(self):
# 		return self.username
print('models finish, user')

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=400, default ='')
	city = models.CharField(max_length=25, default ='')
	state = models.CharField(max_length=2, default ='')
	investor_type = models.CharField(max_length=15, default ='')
	looking = models.BooleanField(default=1)

	def __str__(self):
		return self.user

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

### double check tutorial here for post_save!!!!!!!