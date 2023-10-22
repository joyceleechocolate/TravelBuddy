from . import views
from django.urls import path

urlpatterns = [
    path('trip/', views.TripView.as_view(), name='all_trip'),
    path('trip/<int:pk>/', views.TripView.as_view(), name='single_trip'),
    path('trip/itinerary/', views.ItineraryView.as_view(), name='all_itinerary'),
    path('trip/itinerary/<int:pk>/', views.ItineraryView.as_view(), name='single_itinerary'),
]