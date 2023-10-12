from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self,phone,email,password=None, **extra_fields):
        if not phone:
            raise ValueError("The phone firld must be set")
        if not email:
            raise ValueError("The Email field must be set")
        phone=self.normalize_email(phone)
        email=self.normalize_email(email)
        extra_fields.setdefault('is_active',True)
        user=self.model(phone=phone,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(phone,email,password, **extra_fields)
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone=models.CharField(max_length=15,unique=True)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)

    objects=CustomUserManager()

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=['email']

    def __str__(self) :
        return self.phone


