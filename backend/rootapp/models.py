from django.db import models
from django.contrib.auth.models import User

__models__ = [
    'User',
    'Contact',
    'Phone'
]


# class Contact(models.Model):
#     first_name = models.CharField(max_length=60)
#     middle_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     nick_name = models.CharField(max_length=20)
