from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import index
from .api import endpoints

app_name = 'rootapp'

urlpatterns = [
                  path('', index, name='index'),
              ] + endpoints.urlpatterns

urlpatterns = format_suffix_patterns(urlpatterns)
