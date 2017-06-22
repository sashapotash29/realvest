from django.db import models
from user.models import User
# Create your models here.


# class PropertiesManager(models.Manager):
# 	pass
# # 	def get_queryset(self):
# # 		return super(PropertiesManager, self).get_queryset().filter(term=item)

class Properties(models.Model):
	id = models.AutoField(primary_key=True)
	building_name = models.CharField(max_length=40)
	coordinates = models.CharField(max_length=50)
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
	date_upload = models.DateField()
	image = models.ImageField(upload_to='property_image', blank=True)

	properties = models.Manager()

	def __str__(self):
		return self.address

	def jsonify(self):
		return dict(
			id = self.id, building_name = self.building_name,
			coordinates = self.coordinates, sq_ft = self.sq_ft,
			bedrooms = self.bedrooms, bathrooms = self.bathrooms,
			address = self.address, city = self.city,
			state = self.state, zipcode = self.zipcode,
			past_price = self.past_price, current_price = self.current_price,
			status = self.status, date_upload = str(self.date_upload),
			# image = self.image
			)


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	content = models.CharField(max_length=200)
	datetime = models.DateTimeField()
	prop = models.ForeignKey(Properties, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.content


class UserProp(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	prop = models.ForeignKey(Properties, on_delete=models.CASCADE)

# print('models finish, properties')