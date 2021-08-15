from rest_framework import generics
from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset=Quote.objects.all().order_by('-id')
    serializer_class=QuoteSerializer

class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Quote.objects.all()
    serializer_class=QuoteSerializer