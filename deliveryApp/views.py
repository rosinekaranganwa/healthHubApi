# user_registration/views.py
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer

class SignupView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the passwords match
        if serializer.validated_data["password"] != serializer.validated_data["confirm_password"]:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the 'confirm_password' field as it is not needed in the model
        serializer.validated_data.pop('confirm_password', None)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
