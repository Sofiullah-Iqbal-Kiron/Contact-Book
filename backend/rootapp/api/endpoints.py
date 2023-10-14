from django.urls import path, re_path
from .views import ContactListCreateDestroy, ContactRetrieveUpdateDelete

urlpatterns = [
    path('contacts', ContactListCreateDestroy.as_view(), name='contacts'),
    path('contact/<int:pk>', ContactRetrieveUpdateDelete.as_view(), name='contact-update-delete')
]
