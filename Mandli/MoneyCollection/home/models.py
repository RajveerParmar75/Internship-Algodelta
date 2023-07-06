from django.db import models

# Create your models here.
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
    type = models.CharField(max_length=255)
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


class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class AdminUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class AgentUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Saving_account(models.Model):
    amount = models.PositiveBigIntegerField(default=0)
    agent = models.ForeignKey(AgentUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField(default=0)
    address = models.TextField()


class Saving_Transection(models.Model):
    user= models.ForeignKey(Saving_account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    done_by=models.ForeignKey(AgentUser,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)


class Loan_account(models.Model):
    amount = models.PositiveBigIntegerField(default=0)
    agent = models.ForeignKey(AgentUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField(default=0)
    address = models.TextField()


class Loan_Transection(models.Model):
    user = models.ForeignKey(Loan_account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    done_by = models.ForeignKey(AgentUser, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
