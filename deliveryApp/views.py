from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *

class CustomUserRegistrationView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserRegistrationSerializer

class CustomUserLoginView(ObtainAuthToken):
    serializer_class=CustomUserLoginSerialier

