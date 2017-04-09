from django.db import models

# Create your models here.

class User(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)
	first_name = models.TextField()
	last_name = models.TextField()
	create_date = models.DateTimeField()

	def __str__(self):
		return self.username
print('models finish, user')

