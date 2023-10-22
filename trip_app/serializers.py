from rest_framework import serializers
from .models import Trips, Itinerary
# from django.db import transaction

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Users
#         fields = ('username', 'password', 'email')

class TripsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trips
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    trip_id = TripsSerializer

    class Meta:
        model = Itinerary
        fields = '__all__'
        depth = 1

    