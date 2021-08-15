from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField()
    category=models.CharField(max_length=50)
    subcategory = models.TextField(max_length=50)
    author = models.TextField(max_length=50)

    def title_author(self):
        return self.title + '  ('+ self.author +' )'
    
    def video_num(self):
        return 10
    
    def average_review(self):
        sum=0
        ratings=Rating.objects.filter(video=self)
        if (len(ratings) > 0):
            for rating in ratings:
                sum=rating.stars + sum
            return sum/len(ratings)
        else:
            return 0


    def __str__(self):
        return self.title

class Rating(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField(max_length=300)

       
    class Meta:
        unique_together=(('user', 'video'))
        index_together=(('user', 'video'))

    def __str__(self):
        return self.video.title + '('+ str(self.stars)+ ')'
