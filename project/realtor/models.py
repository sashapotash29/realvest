from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Realtor(User):
	company = models.CharField(max_length=50, default ='Apple Inc.')



	def __str__(self):
		return self.company


		