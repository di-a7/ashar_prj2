from django.urls import path
# from .views import category, categorydetail
from .views import CategoryGenericAPIView, CategoryDetailAPIView
urlpatterns = [
   # Genric api
   path('category/', CategoryGenericAPIView.as_view()),
   path('category/<pk>/', CategoryDetailAPIView.as_view())
   
   # APIView
   # path('category/', CategoryAPIView.as_view()),
   # path('category/<id>/', CategoryDetailAPIView.as_view()),
   
   # function api
   # path('category/', category)
   # path('category/<pk>/', categorydetail)
]