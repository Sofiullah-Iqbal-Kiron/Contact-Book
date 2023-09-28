from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import Contact
from .serializers import ContactSerializer


@api_view()
def index(request):
    return Response({"Message": "This view is for api testing."}, status=status.HTTP_200_OK)


class Contacts(LoginRequiredMixin, APIView):
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
