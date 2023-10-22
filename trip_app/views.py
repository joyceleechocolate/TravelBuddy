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
    
    def Itinerary(self, request):
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
    
    def Itinerary(self, request):
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

# class TripWithItineraryView(APIView):

#     def get(self, request, trippk=None, postpk=None):
#         if postpk:
#             # categories = Category.objects.get(pk=pk)
#             posts = Post.objects.filter(id = postpk, cat_id =catpk)
#             # posts_cat = posts.objects.get(cat_id = catpk)
#             if posts:
#                 serializer = PostSerializer(posts, many=True)
#                 return Response(serializer.data)
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             posts = Post.objects.filter(cat_id = catpk)
#             serializer = PostSerializer(posts, many=True)
#             return Response(serializer.data)
    
#     def post(self, request, catpk, postpk):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, catpk, postpk):
#         try:
#             post = Post.objects.get(id=postpk, cat_id = catpk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, catpk, postpk):
#         try:
#             post = Post.objects.get(id=postpk, cat_id=catpk)
#         except Post.DoesNotExist:
#             return Response('The post has been deleted!', status=status.HTTP_404_NOT_FOUND)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  