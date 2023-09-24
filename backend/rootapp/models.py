from django.db import models
from django.contrib.auth.models import User

from .validators import phone_number_validator
from .constants import CountryCodes, largest_country_code

__models__ = [
    "User",
    "Contact",
    "Phone"
]


class Contact(models.Model):
    of = models.ForeignKey(User, models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=20)
    email = models.EmailField('personal email', null=True, blank=True)
    website = models.URLField('person personal website, if any', null=True, blank=True)
    relation = models.CharField('relation with current user', max_length=100, null=True, blank=True)
    avatar = models.ImageField('Person picture', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField('Full address', null=True, blank=True)
    about = models.CharField('abstract, company or short details', max_length=100)
    details = models.TextField('more about')

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name


class Phone(models.Model):
    of = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='numbers')
    country_code = models.CharField(choices=CountryCodes, default="+880", max_length=largest_country_code)
    number = models.CharField('cell number', max_length=11, validators=[phone_number_validator])
    label = models.CharField('number kind/label', max_length=60)

    def __str__(self):
        return str(self.of)
