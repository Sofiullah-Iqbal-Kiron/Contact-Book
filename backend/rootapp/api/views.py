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


class ContactRetrieveCreateDestroy(LoginRequiredMixin, APIView):
    """
    List all contacts of requested user, Create a single one and Destroy all at one go.
    """

    def get(self, request, format=None):
        # contacts = Contact.objects.filter(of=request.user)
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = ContactSerializer(data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        # destroy all, take confirmation, move to trash for 30 days
        pass


class ContactUpdateDestroy(LoginRequiredMixin, APIView):
    def post(self, request, pk, format=None):
        # update
        pass

    def delete(self, request, pk, format=None):
        # destroy
        pass
