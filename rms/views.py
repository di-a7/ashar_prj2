from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, OrderItem
from .serializers import CategorySerializer
from rest_framework import status
# Create your views here.

# Class Based API
# APIView
from rest_framework.views import APIView

class CategoryAPIView(APIView):
   def get(self,request):
      category = Category.objects.all()
      serializer = CategorySerializer(category, many=True)
      return Response(serializer.data)
   
   def post(self,request):
      serializer = CategorySerializer(data=request.data)   # deserialization: convert json data into python data
      serializer.is_valid(raise_exception = True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryDetailAPIView(APIView):
   def get(self,request,pk):
      category = Category.objects.get(pk=pk)
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   
   def delete(self,request,pk):
      category = Category.objects.get(pk=pk)
      item = OrderItem.objects.filter(food__category = category).count()
      if item > 0 :
         return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
      category.delete()
      return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)
   
   def put(self,request,pk):
      category = Category.objects.get(pk=pk)
      serializer = CategorySerializer(category, data=request.data)
      serializer.is_valid(raise_exception = True)
      serializer.save()
      return Response(serializer.data)
   
   def patch(self,request,pk):
      category = Category.objects.get(pk=pk)
      serializer = CategorySerializer(category, data=request.data, partial=True)
      serializer.is_valid(raise_exception = True)
      serializer.save()
      return Response(serializer.data)




# Functioin Based API
# @api_view(['GET','POST'])
# def category(request):
#    if request.method == 'GET':
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True) # serializer: convert queryset into json format
#       return Response(serializer.data)

#    elif request.method == 'POST':
#       serializer = CategorySerializer(data=request.data)   # deserialization: convert json data into python data
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def categorydetail(request, pk):
#    category = Category.objects.get(pk=pk)
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method == 'DELETE':
#       item = OrderItem.objects.filter(food__category = category).count()
#       if item > 0 :
#          return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
#       category.delete()
#       return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)
   
#    elif request.method == 'PUT':       # requires all fields to be sent in the request body
#       serializer = CategorySerializer(category, data=request.data)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data)
   
#    elif request.method == 'PATCH':     # requires only the fields to be sent in the request body that need to be updated
#       serializer = CategorySerializer(category, data=request.data, partial=True)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data)

# table function: GET, POST, RETRIEVE,PUT,DELETE