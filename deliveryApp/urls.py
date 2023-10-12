from django.urls import path
from .views import *

urlpatterns = [
    path('register/', CustomUserRegistrationView.as_view(), name='user-register'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
]
