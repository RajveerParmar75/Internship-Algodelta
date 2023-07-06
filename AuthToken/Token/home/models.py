from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


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
    is_staff = models.IntegerField()
    mac = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
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


class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class LoginUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Session(models.Model):
    token = models.CharField(max_length=500)
    user_id = models.IntegerField()
    mac = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


class State(models.Model):
    state_name = models.CharField(max_length=50)


class City(models.Model):
    city_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
class BlackListToken(models.Model):
    token = models.CharField(max_length=500)