from django.db import models
# from accounts.models import Users

# Create your models here.
# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)

class Trips(models.Model):
    trip_name = models.CharField(max_length=255)
    # user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Itinerary(models.Model):
    trip_id = models.ForeignKey(Trips, on_delete=models.CASCADE)
    travel_date_begin = models.DateField()
    travel_date_end = models.DateField()
    travel_location = models.CharField(max_length=255)
    travel_duration = models.CharField(max_length=255)
    detail_itinerary = models.TextField()

