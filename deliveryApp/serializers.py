from rest_framework import serializers
from .models import *

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('phone','email','password')
        extra_kwargs={'password':{'write_only': True}}

    def create(self, validated_data):
        user=CustomUser(
            phone=validated_data['phone'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save
        return user
    
class CustomUserLoginSerialier(serializers.Serializer):
    phone=serializers.CharField()
    password=serializers.CharField()
        


