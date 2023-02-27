from django.urls import path, include
from .views import *

urlpatterns = [    
   path('', Retaurants.as_view(), name = 'get_restaurants')
]
