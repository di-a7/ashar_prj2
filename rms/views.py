from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .pagination import FoodPagination
# Create your views here.

# Class Based API
# ModelViewset
from rest_framework import viewsets
class CategoryModelViewset(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   pagination_class = PageNumberPagination
   
   def destroy(self,request,pk):
      category = Category.objects.get(pk=pk)
      item = OrderItem.objects.filter(food__category = category).count()
      if item > 0 :
         return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
      category.delete()
      return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)


class FoodModelViewset(viewsets.ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = FoodPagination




# Viewset
# class CategoryViewset(viewsets.ViewSet):
#    def list(self,request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def create(self,request):
#       serializer = CategorySerializer(data=request.data)   # deserialization: convert json data into python data
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

#    def retrieve(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    def destroy(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       item = OrderItem.objects.filter(food__category = category).count()
#       if item > 0 :
#          return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
#       category.delete()
#       return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)
   
#    def update(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category, data=request.data)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def partial_update(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category, data=request.data, partial=True)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data)


# Concrete View Classes
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# class CategoryGenericAPIView(ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

# class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def delete(self, request, pk):
#       category = Category.objects.get(pk=pk)
#       item = OrderItem.objects.filter(food__category = category).count()
#       if item > 0 :
#          return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
#       category.delete()
#       return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)



# GenericAPI and Mixin
# from rest_framework.generics import GenericAPIView, mixins
# class CategoryGenericAPIView(GenericAPIView, mixins.ListModelMixin):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def get(self,request):
#       return self.list(request)
   
   # def post(self,reqeust):
   #    return self.create(self.request)

# class CategoryDetailAPIView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def get(self,request, pk):
#       return self.retrieve(request, pk)
   
#    def put(self, request, pk):
#       return self.update(request, pk)
   
#    def patch(self, request, pk):
#       return self.partial_update(request, pk)
      
#    def delete(self, request, pk):
#       category = Category.objects.get(pk=pk)
#       item = OrderItem.objects.filter(food__category = category).count()
#       if item > 0 :
#          return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
#       category.delete()
#       return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)

# GenericAPIView
# class CategoryGenericAPIView(GenericAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def get(self,request):
#       category = self.get_queryset()
#       serializer = self.get_serializer(category, many=True)
#       return Response(serializer.data)
   
#    def post(self,request):
#       pass

# class CategoryDetail(GenericAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def get(self, request, pk):
#       category = self.get_object()
#       serializer = self.get_serializer(category)
#       return Response(serializer.data)








# APIView
# from rest_framework.views import APIView

# class CategoryAPIView(APIView):
#    def get(self,request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many=True)
#       return Response(serializer.data)
   
#    def post(self,request):
#       serializer = CategorySerializer(data=request.data)   # deserialization: convert json data into python data
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

# class CategoryDetailAPIView(APIView):
#    def get(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    def delete(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       item = OrderItem.objects.filter(food__category = category).count()
#       if item > 0 :
#          return Response({"message":"Can not be deleted. Category related to Food in OrderItem."})
#       category.delete()
#       return Response({"message":"Data deleted."}, status=status.HTTP_204_NO_CONTENT)
   
#    def put(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category, data=request.data)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def patch(self,request,pk):
#       category = Category.objects.get(pk=pk)
#       serializer = CategorySerializer(category, data=request.data, partial=True)
#       serializer.is_valid(raise_exception = True)
#       serializer.save()
#       return Response(serializer.data)




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