from django.urls import path,include
from quotes.api.views import QuoteListCreateView, QuoteDetailView

# all api urls base is stored here
urlpatterns = [
    
    path('jobs/', include('jobs.api.urls')),
    path('quotes/', include('quotes.api.urls')),
    path('ebooks/', include('ebooks.api.urls')),
    path('videos/', include('videos.api.urls')),
]
