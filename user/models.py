from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
   phone = models.CharField(max_length=15, unique = True)
   
   USERNAME_FIELD = "phone"