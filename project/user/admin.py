from django.contrib import admin
# from user.models import User
# Register your models here.
# admin.site.register(User)


@app.route('/<token>', methods = ['POST'])        
def add_listing(token):    
    new_listing = {
    'street_address': request.json['street_address'],
    'city' : request.json['city'],
    'state': request.json['state'],
    'zip' : request.json['zip'],
    'price': request.json['price'],
    'num_of_bedrooms': request.json['num_of_bedrooms'],
    'num_of_bathrooms' : request.json['num_of_bathrooms'],
    'amenities': request.json['amenities'],
    'description' : request.json['description'],
    'date_listed': datetime.datetime.now(),
    'rental_or_sale' : request.json['rental_or_sale'],
    'available or sold': request.json['available_or_sold'],
    'agent_token' : token,
    'square_feet': request.json['square_feet']
    }
    
    enter_new_listing(token,new_listing)
    return('ballin!')