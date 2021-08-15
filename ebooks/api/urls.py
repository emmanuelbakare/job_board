from django.urls import path
from ebooks.api.views import EbookView,EbookDetailView, ReviewView
urlpatterns = [
    path('', EbookView.as_view(), name="book-list"),
    path('<int:pk>/', EbookDetailView.as_view(), name="book-detail"),
    path('<int:book_id>/reviews/', ReviewView.as_view(), name="book-reviews"),
]
