from jobs.api.views import JobOfferGenericView
from django.urls import path

urlpatterns = [
    path('', JobOfferGenericView.as_view(), name="jobs-api")
]
