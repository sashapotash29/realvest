from django.db import models
from django.contrib.auth.models import User
from properties.models import Properties
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

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=400, default ='')
	city = models.CharField(max_length=25, default ='')
	state = models.CharField(max_length=2, default ='')
	investor_type = models.CharField(max_length=15, default ='')
	looking = models.BooleanField(default=1)
	image = models.ImageField(upload_to='profile_image', blank=True)
	investor = models.BooleanField(default = True) # If this field is False, then the user is a Realtor. Else, User is a Investor.

	user_manager = models.Manager()

	def __str__(self):
		return self.user.username


	def get_all_investgroups(self):
		pass


class SavedProperities(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)



class DirectGroup(models.Model):
	prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
	investor_id = models.ForeignKey(User, on_delete=models.CASCADE)
	realtor_id =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="realtor_id")




def create_profile(sender, **kwargs):
	print(dir(UserProfile))
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

# x = UserProfile.userprofile.all()
# print(x[0])
# print(dir(x[0]))
# print(x[0].user)
# print(dir(x[0].user))


### double check tutorial here for post_save!!!!!!!