from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .apiviews import LogoutAPI, RegistrationAPI

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegistrationAPI.as_view(), name='register'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
]
