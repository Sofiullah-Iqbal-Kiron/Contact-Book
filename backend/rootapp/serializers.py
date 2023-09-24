from rest_framework import serializers

from .models import Contact, Phone


class NumberSerializer(serializers.ModelSeiralizer):
    class Meta:
        model = Phone
        fields = ['number', 'label']


class ContactSerialier(serializers.ModelSerializer):
    numbers = NumberSerializer(many=True)

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name']
