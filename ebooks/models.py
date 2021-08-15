from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Ebook(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description= models.TextField()
    publication_date=models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    review_author=models.CharField(max_length=50, blank=True, null=True)
    review=models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    book = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.rating
