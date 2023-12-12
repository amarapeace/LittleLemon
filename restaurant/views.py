from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer



      
 
        
#   using the generic view for menu   
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# using the APIView for booking
# class BookingView(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serialized = BookingSerializer(items, many=True)
#         return Response(serialized.data)


# using th APIView for menu
# class MenuView(APIView):
#     def post(self, request):
#         serialized = MenuSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response({"status":"success","data":  serialized.data}) 