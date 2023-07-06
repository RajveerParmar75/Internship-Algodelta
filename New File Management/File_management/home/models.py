from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
class Organization(models.Model):
    org_name=models.CharField(max_length=100)
class State(models.Model):
    state_name=models.CharField(max_length=100)
class City(models.Model):
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100)
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', 0)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.CharField(max_length=255)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
    def __str__(self):
        return self.email

class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
class User(models.Model):
    pass
class Document(models.Model):
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    org_id=models.ForeignKey(Organization,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)