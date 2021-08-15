from rest_framework import mixins
from rest_framework import generics

from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer

class JobOfferGenericView(generics.ListCreateAPIView):
    queryset= JobOffer.objects.all()
    serializer_class=JobOfferSerializer
# class JobOfferGenericView(mixins.ListModelMixin,
#                           mixins.CreateModelMixin,
#                           generics.GenericAPIView):
#     queryset=JobOffer.objects.all()
#     serializer_class=JobOfferSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request,*args, **kwargs)
    
#     def post(self, request, *args, **kwargs ):
#         return self.create( request, *args, **kwargs )