from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission




class User(AbstractUser):
    # Your custom fields and methods

    class Meta:
        db_table = 'user_table'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        default_permissions = ()
        permissions = []

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='home_users'  # Add a unique related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='home_users'  # Add a unique related_name
    )
class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name