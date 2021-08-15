from django.urls import path, include
from rest_framework import  routers
from videos.api.views import VideoViewset, RatingViewset

router= routers.DefaultRouter()

router.register('', VideoViewset) 

urlpatterns = [
    path('', include(router.urls))
    
]
