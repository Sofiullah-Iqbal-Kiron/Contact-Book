from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import Contact
from .serializers import ContactSerializer


class ContactListCreateDestroy(APIView):
    """
    List your all contacts.
    Create a single one.
    Destroy all contacts, todo: move to trash for 30 days.
    """

    def get(self, request, format=None):
        """List your contacts."""
        # contacts = Contact.objects.filter(of=request.user)
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Create a contact."""
        data = request.data
        serializer = ContactSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(of=request.user)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        """ Delete all contacts of currently logged in user. """
        # https://docs.djangoproject.com/en/4.2/topics/db/queries/#deleting-objects
        count_deleted, object_count = Contact.objects.filter(of=request.user).delete()
        return Response({'message': f'{count_deleted} contacts deleted'}, status=status.HTTP_200_OK)


class ContactRetrieveUpdateDelete(APIView):
    """
    Single operation allowed endpoint.
    Update and Delete a contact, single one per hit.
    Allowed methods: GET, PUT, DELETE
    GET: Retrieve contact of that id.
    PUT: Update contact of this id provided within url.
    DELETE: Delete the contact of that id.

    Date input format: "YYYY-MM-DD"
    """

    def get_instance(self, pk):
        try:
            instance = Contact.objects.get(pk=pk)
            return instance
        except Contact.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        """ Retrieve """
        instance = self.get_instance(pk=pk)
        if instance is not None:
            serializer = ContactSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'errors': 'contact within this id is not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request: Request, pk: int, format=None):
        """ Update """
        instance: Contact = self.get_instance(pk=pk)
        if instance is not None:
            serializer = ContactSerializer(instance=instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'errors': 'contact within this id not found, no update happened'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        """ Delete """
        instance = self.get_instance(pk)
        if instance is not None:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'errors': 'no contact available within this id, so no delete operation executed'}, status=status.HTTP_204_NO_CONTENT)
