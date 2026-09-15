from django.urls import path
# from .views import category, categorydetail
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"category", CategoryModelViewset, basename="category")
router.register(r"food", FoodModelViewset, basename="food")

urlpatterns = [
   # Viewset api
   # path('category/', CategoryViewset.as_view({'get':'list','post':'create'})),
   # path('category/<pk>/', CategoryDetailViewset.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'}))
   
   # APIView/GernericAPIView
   # path('category/', CategoryAPIView.as_view()),
   # path('category/<id>/', CategoryDetailAPIView.as_view()),
   
   # function api
   # path('category/', category)
   # path('category/<pk>/', categorydetail)
] + router.urls