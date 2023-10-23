from . import views
from django.urls import path

urlpatterns = [
    path('trips/', views.TripView.as_view(), name='all_trip'),
    path('trips/<int:pk>/', views.TripView.as_view(), name='single_trip'),
    path('trips/<int:trippk>/itinerary/', views.TripWithItineraryView.as_view(), name='trip_itineraries'),
    path('trips/<int:trippk>/itinerary/<int:intpk>/', views.TripWithItineraryView.as_view(), name='trip_itinerary'),
    path('trips/itinerary/', views.ItineraryView.as_view(), name='all_itinerary'),
    # path('trip/itinerary/<int:pk>/', views.ItineraryView.as_view(), name='single_itinerary'),
]