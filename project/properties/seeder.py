from datetime import date
from .models import Properties

### only used for seeding data____________
def seed_prop_to_db(data):
	print('seed func')
	prop = Properties(
				building_name = data['building_name'],
				longitude =  data['longitude'],
				latitude = data['latitude'],
				sq_ft = data['sq_ft'],
				bedrooms = data['bedrooms'],
				bathrooms = data['bathrooms'],
				address = data['address'],
				city = data['city'],
				state = data['state'],
				zipcode = data['zipcode'],
				past_price = 0.0,
				current_price = data['current_price'],
				status = 'available',
				date_upload = date.today()
	)	
	print(prop)
	prop.save()
	print('property saved')