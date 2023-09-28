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
    # reverse from Phone: numbers
    of = models.ForeignKey(User, models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    nick_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(verbose_name='personal email', null=True, blank=True)
    website = models.URLField(verbose_name='personal website, if any', null=True, blank=True)
    relation = models.CharField(verbose_name='relation with current user', max_length=100, null=True, blank=True)
    avatar = models.ImageField(verbose_name='person picture', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(verbose_name='full address', null=True, blank=True)
    about = models.CharField(verbose_name='company, abstract or short details', max_length=100, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

    class Meta:
        ordering = ['first_name']


class Phone(models.Model):
    of = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='numbers')
    country_code = models.CharField(choices=CountryCodes, default="BD", max_length=largest_country_code)
    number = models.CharField(max_length=30, validators=[phone_number_validator], unique=True)
    label = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.number + ' : ' + self.of.first_name + ' ' + self.of.middle_name + ' ' + self.of.last_name

    class Meta:
        ordering = ['number']
