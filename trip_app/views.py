from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class TripView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            trip = Trips.objects.get(pk=pk)
            if trip is not None:
                serializer = TripsSerializer(trip)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            trip = Trips.objects.all()
            serializer = TripsSerializer(trip, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = TripsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            trip = Trips.objects.get(pk=pk)
        except Trips.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TripsSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            trip = Trips.objects.get(pk=pk)
        except Trips.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        trip.delete()
        return Response('The trip has been deleted!',status=status.HTTP_204_NO_CONTENT)

class ItineraryView(APIView):

    def get(self, request, pk=None):
        if pk:
            dailySchedule = Itinerary.objects.get(pk=pk)
            if dailySchedule:
                serializer = ItinerarySerializer(dailySchedule)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            dailySchedule = Itinerary.objects.all()
            serializer = ItinerarySerializer(dailySchedule, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            dailySchedule = Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItinerarySerializer(dailySchedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            dailySchedule = Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        dailySchedule.delete()
        return Response('The itinerary has been deleted!', status=status.HTTP_204_NO_CONTENT)

class TripWithItineraryView(APIView):

    def get(self, request, trippk=None, intpk=None):
        if trippk is not None and intpk is not None:
            #both trippk and intpk are provided, filter by both parameters
            itinerary = Itinerary.objects.filter(trip_id = trippk, id =intpk)
        
        elif trippk is not None:
            #only trippk is provided, filter by trip_id
            itinerary = Itinerary.objects.filter(trip_id=trippk)
        else: 
            #Neither pk provided, return all
            itinerary = Itinerary.objects.all()  
        serializer = ItinerarySerializer(itinerary, many=True)
        return Response(serializer.data)

    def post(self, request, trippk):
        if trippk is None:
            return Response({'error': 'trippk is required to create an itinerary.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the trip with the specified trippk exists
        try:
            trip = Trips.objects.get(pk=trippk)
        except Trips.DoesNotExist:
            return Response({'error': 'Trip does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['trip_id'] = trip  # Associate the trip with the itinerary
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, trippk, intpk):
        try:
            itinerary = Itinerary.objects.get(id=intpk, trip_id = trippk)
        except Itinerary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ItinerarySerializer(itinerary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, trippk, intpk):
        try:
            itinerary = Itinerary.objects.get(id=intpk, trip_id=trippk)
        except Itinerary.DoesNotExist:
            return Response('The requested itinerary does not exist.', status=status.HTTP_404_NOT_FOUND)
        itinerary.delete()
        return Response('The itinerary has been deleted!',status=status.HTTP_204_NO_CONTENT)  