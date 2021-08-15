from rest_framework import serializers
from  videos.models import Video, Rating 

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        # fields = "__all__"
        fields = ['title','description','url', 'category','subcategory','author','average_review','title_author', 'video_num']
    

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Rating 
        fields = "__all__"
