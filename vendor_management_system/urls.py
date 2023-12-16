from django.contrib import admin
from django.urls import path, include
from vendor_api.signals import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendor_api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('',include('user_app.urls'))
]
