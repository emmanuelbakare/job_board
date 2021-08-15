from django.urls import path 
from quotes.api.views import QuoteListCreateView, QuoteDetailView

urlpatterns = [
    path('',QuoteListCreateView.as_view(), name="quote-list"),
    path('<int:pk>/',QuoteDetailView.as_view(), name="quote-detail"),
    
]
