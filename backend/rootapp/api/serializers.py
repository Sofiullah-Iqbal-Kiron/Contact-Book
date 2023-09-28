from rest_framework import serializers

from rootapp.models import Contact, Phone


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        exclude = ['id', 'of']


class ContactSerializer(serializers.ModelSerializer):
    numbers = NumberSerializer(many=True)

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'nick_name',
            'numbers'
        ]
