import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel_proj.settings")
django.setup()

from trip_app.models import Trips, Itinerary
from accounts.models import Users  

#insert data into Users

user_data = [
    {
    {'username': 'testing1'},
    {'password': '1234'},
    {'email': 'testing1@codeplatoon.com' },
    },

    {
    {'username': 'testing2'},
    {'password': '2234'},
    {'email': 'testing2@codeplatoon.com' },
    },
]

for data in user_data:
    Users.objects.create(username=data['username'], password=data['password'], email=data['email'])

print('User data has been created successfully!') 

#insert data into Trips

trips_data = [
    {
    {'trip_name': 'Alaska'},
    {'user_id': 1},
    },

    {
    {'trip_name': 'Iceland'},
    {'user_id': 1},
    },

    {
    {'trip_name': 'Berlin'},
    {'user_id': 2},
    },
]

# def insert_post_data(user_id):
#     category = Categories.objects.get(pk=category_id)
#     for data in post_data:
#         Post.objects.create(category=category, **data)

# for entry in category_data:
#     insert_post_data(entry['category_id'], entry['post_data'])

for data in trips_data:
    Trips.objects.create(trip_name=data['trip_name'], user_id=data['user_id'])

print('Trips data has been created successfully!') 

#insert itinerary data

itinerary_data = [
    {
    {'trip_id': 1},
    {'travel_date_begin': '05/02/2024'},
    {'travel_date_end': '05/12/2024'},
    {'travel_location': 'Alaska, USA'},
    {'travel_duration': '11 Days'},
    {'detail_itinerary': 'Day1: Flying. Day2: Visit Glaciers. Day3: Feast on salmons and king crabs.'},
    },

    {
    {'trip_id': 2},
    {'travel_date_begin': '03/11/2024'},
    {'travel_date_end': '003/17/2024'},
    {'travel_location': 'Iceland'},
    {'travel_duration': '7 Days'},
    {'detail_itinerary': 'Testing travel itinerary - Iceland'},
    },

    {
    {'trip_id': 3},
    {'travel_date_begin': '01/15/2024'},
    {'travel_date_end': '01/20/2024'},
    {'travel_location': 'Berling, Germany'},
    {'travel_duration': '6 Days'},
    {'detail_itinerary': 'Testing travel itinerary - Berlin'},
    },
]

for data in itinerary_data:
    Itinerary.objects.create(trip_id=data['trip_id'], travel_date_begin=data['travel_date_begin'], travel_date_end=data['travel_date_end'], travel_location=data['travel_location'], travel_duration=data['travel_duration'], detail_itinerary=data['detail_itinerary'])

print('Itinerary data has been created successfully!') 