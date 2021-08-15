from rest_framework import generics
from ebooks.models import Ebook,Review
from rest_framework.generics import get_object_or_404
from ebooks.api.serializers import EbookSerializer, ReviewSerializer

class EbookView(generics.ListCreateAPIView):
    queryset= Ebook.objects.all()
    serializer_class=EbookSerializer

class EbookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Ebook.objects.all()
    serializer_class=EbookSerializer

class ReviewView(generics.ListCreateAPIView):
    queryset= Review.objects.all()
    serializer_class=ReviewSerializer

    def perform_create(self, serializer):
        book_id=self.kwargs.get('book_id')
        ebook=get_object_or_404(Ebook, pk=book_id)
        serializer.save(book=ebook)


