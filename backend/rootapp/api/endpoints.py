from django.urls import path
from .views import ContactRetrieveCreateDestroy

urlpatterns = [
    path('contacts', ContactRetrieveCreateDestroy.as_view(), name='contacts')
]
