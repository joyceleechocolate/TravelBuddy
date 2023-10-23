from rest_framework import serializers
from .models import Trips, Itinerary
from django.db import transaction

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
        fields = ['trip_id', 
                  'travel_date_begin', 
                  'travel_date_end', 
                  'travel_location', 
                  'travel_duration', 
                  'detail_itinerary']
        depth = 1

    def create(self, validated_data):
        trip_data = validated_data.pop('trip_id')
        if not trip_data:
            raise serializers.ValidationError({'trip_id': 'Trip data is required.'})
        with transaction.atomic():
            trip, created = Trips.objects.get_or_create(trip_name=trip_data.trip_name)
            itinerary = Itinerary.objects.create(trip_id=trip, **validated_data)
        return itinerary
    
    def update(self, instance, validated_data):
        trip_data = validated_data.get('trip_id') 
        if trip_data:
            trip, created = Trips.object.get_or_create(**trip_data)
            instance.trip_id = trip
        # trip, created = Trips.objects.get_or_create(**trip_data)
        # instance.trip_id = trip
        instance.travel_date_begin = validated_data.get('travel_date_begin', instance.travel_date_begin)
        instance.travel_date_end = validated_data.get('travel_date_end', instance.travel_date_end)
        instance.travel_location = validated_data.get('travel_location', instance.travel_location)
        instance.travel_duration = validated_data.get('travel_duration', instance.travel_duration)
        instance.detail_itinerary = validated_data.get('detail_itinerary', instance.detail_itinerary)
        instance.save()
        return instance