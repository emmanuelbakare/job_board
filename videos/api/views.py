from rest_framework import viewsets
from videos.models import Video, Rating
from videos.api.serializers import VideoSerializer, RatingSerializer

class RatingViewset(viewsets.ModelViewSet):
    queryset= Rating 
    serializer_class = RatingSerializer

class VideoViewset(viewsets.ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

