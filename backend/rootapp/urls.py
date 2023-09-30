from django.urls import path

from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import index
from .api import endpoints

app_name = 'rootapp'

schema_view = get_schema_view(
    openapi.Info(
        title="Contacts API",
        default_version='v1',
        description="Test Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="example@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

documentation_paths = [
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), # collision with tick-1
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns = documentation_paths + urlpatterns
urlpatterns = urlpatterns + endpoints.urlpatterns
urlpatterns = format_suffix_patterns(urlpatterns) # tick-1
