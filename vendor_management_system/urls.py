from django.contrib import admin
from django.urls import path, include
from vendor_api.signals import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Vendor Management System",
        default_version='v1.0.0',
        description="Vendor Management System api documentation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="rishikesh.karn@outlook.com"),
        license=openapi.License(name="Rishikesh Kumar"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendor_api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include('user_app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
