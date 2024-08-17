from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

app_name='restauranst'
urlpatterns=[
    path('api-auth-token/',obtain_auth_token),
  

]