from django.urls import path
# from .views import category, categorydetail
from .views import CategoryAPIView
urlpatterns = [
   path('category/', CategoryAPIView.as_view()),
   
   # function api
   # path('category/', category)
   # path('category/<pk>/', categorydetail)
]