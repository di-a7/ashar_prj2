from django.urls import path
from .views import category, categorydetail

urlpatterns = [
   path('category/', category),
   path('category/<pk>/', categorydetail)
]