from django.db import models
from user.models import User
from datetime import datetime
# Create your models here.


# class PropertiesManager(models.Manager):
# 	pass
# # 	def get_queryset(self):
# # 		return super(PropertiesManager, self).get_queryset().filter(term=item)

class Properties(models.Model):
	id = models.AutoField(primary_key=True)
	building_name = models.CharField(max_length=40)
	longitude = models.CharField(max_length=40)
	latitude = models.CharField(max_length=40)
	sq_ft = models.FloatField()
	bedrooms = models.FloatField()
	bathrooms = models.FloatField()
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.IntegerField()
	past_price = models.FloatField()
	current_price = models.FloatField()
	status = models.CharField(max_length=10)
	date_upload = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to='property_image', blank=True)
	realtor_id = models.ForeignKey(User, on_delete=models.CASCADE, default = 1) # Remove default in production setting


	properties = models.Manager()

	def __str__(self):
		return self.address

	def jsonify(self):
		return dict(
			id = self.id, building_name = self.building_name,
			longitude = self.longitude,
			latitude = self.latitude, sq_ft = self.sq_ft,
			bedrooms = self.bedrooms, bathrooms = self.bathrooms,
			address = self.address, city = self.city,
			state = self.state, zipcode = self.zipcode,
			past_price = self.past_price, current_price = self.current_price,
			status = self.status, date_upload = str(self.date_upload),
			# image = self.image
			)


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	content = models.CharField(max_length=500)
	datetime = models.DateTimeField(auto_now_add = True)
	prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.content


class Investment(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	prop = models.ForeignKey(Properties, on_delete=models.CASCADE)
	amount = models.FloatField()


# print('models finish, properties')




# print('models finish, properties')

