from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, OrderItem
from .serializers import CategorySerializer
# Create your views here.

@api_view(['GET','POST'])
def category(request):
   if request.method == 'GET':
      category = Category.objects.all()
      serializer = CategorySerializer(category, many=True) # serializer: convert queryset into json format
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = CategorySerializer(data=request.data)   # deserialization: convert json data into python data
      serializer.is_valid(raise_exception = True)
      serializer.save()
      return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def categorydetail(request, pk):
   category = Category.objects.get(pk=pk)
   if request.method == 'GET':
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   elif request.method == 'DELETE':
      item = OrderItem.objects.filter(food__category = category).count()
      if item > 0 :
         return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
      category.delete()
      return Response({"message":"Data deleted."})
   elif request.method == 'PUT':       # requires all fields to be sent in the request body
      serializer = CategorySerializer(category, data=request.data)
      serializer.is_valid(raise_exception = True)
      serializer.save()
      return Response(serializer.data)
   elif request.method == 'PATCH':     # requires only the fields to be sent in the request body that need to be updated
      serializer = CategorySerializer(category, data=request.data, partial=True)
      serializer.is_valid(raise_exception = True)
      serializer.save()
      return Response(serializer.data)

# table function: GET, POST, RETRIEVE,PUT,DELETE