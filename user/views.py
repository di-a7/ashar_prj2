from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

class LoginAPIView(APIView):
   def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      # add: check if both username and password are not empty, if empty raise an exception: both field are required, if exist check in database
      user = authenticate(username = username, password = password)   # User.objects.filter(username = username, password = password)
      if user:
         token,_ = Token.objects.get_or_create(user = user)   #('token',create_statue(True/False))
         return Response({'token':token.key, 'username':username})
      return Response({"details":"Invalid Credential"})