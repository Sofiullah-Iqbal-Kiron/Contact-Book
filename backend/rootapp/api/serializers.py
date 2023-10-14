from django.utils import timezone

from rest_framework import serializers

from rootapp.models import Contact, Phone


class NumberListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        numbers = [Phone(**number) for number in validated_data]
        return Phone.objects.bulk_create(numbers)


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        exclude = ['id', 'of']
        list_serializer_class = NumberListSerializer


# read this docs first of all ok to fine man
# https://www.django-rest-framework.org/api-guide/serializers/#writing-create-methods-for-nested-representations
class ContactSerializer(serializers.ModelSerializer):
    numbers = NumberSerializer(many=True)
    date_of_birth = serializers.DateField(format="%d %B %Y", required=False)
    created_at = serializers.DateTimeField(format="%d %B %Y (%I:%M %p)", read_only=True)

    class Meta:
        model = Contact
        fields = [
            'id',
            'numbers',
            'first_name',
            'middle_name',
            'last_name',
            'nick_name',
            'email',
            'website',
            'relation',
            'avatar',
            'date_of_birth',
            'address',
            'about',
            'details',
            'created_at'
        ]

    def create(self, validated_data):
        numbers = validated_data.pop('numbers')
        numbers_serializer = NumberSerializer(data=numbers, many=True)
        numbers_serializer.is_valid(raise_exception=True)
        contact: Contact = Contact.objects.create(**validated_data)
        ret_nums = numbers_serializer.save(of=contact)
        contact.numbers.set(ret_nums)
        return contact

    def update(self, instance: Contact, validated_data):
        instance.numbers.all().delete()
        # it should be multiple updates, not delete all previous and creating new instances
        # https://www.django-rest-framework.org/api-guide/serializers/#customizing-multiple-update
        # head over to: https://github.com/beda-software/drf-writable-nested
        numbers = validated_data.pop('numbers')
        numbers_serializer = NumberSerializer(data=numbers, many=True)
        numbers_serializer.is_valid()
        numbers = numbers_serializer.save(of=instance)

        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.middle_name=validated_data.get('middle_name',instance.middle_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.nick_name=validated_data.get('nick_name',instance.nick_name)
        instance.email=validated_data.get('email',instance.email)
        instance.website=validated_data.get('website',instance.website)
        instance.relation=validated_data.get('relation',instance.relation)
        instance.avatar=validated_data.get('avatar',instance.avatar)
        instance.date_of_birth=validated_data.get('date_of_birth', instance.date_of_birth)
        instance.address=validated_data.get('address',instance.address)
        instance.about=validated_data.get('about',instance.about)
        instance.details=validated_data.get('details',instance.details)

        instance.save()
        return instance
