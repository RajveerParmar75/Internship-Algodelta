from django.db import models
class MonitorMobel(models.Model):
    request=models.CharField(max_length=100)
    organization_id=models.IntegerField(default=0)
class OrganizationModel(models.Model):
    organization_name = models.CharField(max_length=50)
    space=models.IntegerField(default=1048576)
    def __str__(self):
        return self.id
class SpaceModel(models.Model):
    organization_id = models.IntegerField(default=0)
    space = models.IntegerField(default=1048576)
class State(models.Model):
    state_name=models.CharField(max_length=50)
class CityModel(models.Model):
    city_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
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
    type_user=models.IntegerField(default=0)
    city=models.IntegerField(default=0)
    state = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    mobile_number= models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.CharField(max_length=255)
    organization_name=models.IntegerField(default=0)
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
class User_TypeModel(models.Model):
    type=models.CharField(max_length=50)
