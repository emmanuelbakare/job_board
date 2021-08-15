from django.contrib import admin
from videos.models import Rating, Video
# Register your models here.

admin.site.register(Video)
admin.site.register(Rating)
