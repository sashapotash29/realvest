from django.db import models
from user.models import User
from properties.models import Properties 
# Create your models here.


class Group(models.Model):
	id = models.AutoField(primary_key=True)
	prop = models.ForeignKey(Properties, on_delete=models.CASCADE)

	def __str__(self):
		return self.prop

class Message(models.Model):
	id = models.AutoField(primary_key=True)
	content = models.TextField()
	date = models.DateField()
	time = models.TimeField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

	def __str__(self):
		return self.content
		
print('models finish, messenger')