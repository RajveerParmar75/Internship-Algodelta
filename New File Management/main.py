import pytz
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
import datetime
from cryptography.fernet import Fernet
from rest_framework.exceptions import ValidationError

local_tz = pytz.timezone("Asia/Kolkata")


def get_local_date_with_gap():
    return datetime.date.today() + datetime.timedelta(days=30)


def generate_encryption_key():
    return Fernet.generate_key().decode()


class AdminUser(models.Model):
    username = models.CharField(verbose_name="User email", max_length=200)


class UserManager(BaseUserManager):
    def create_user(self, username, password, content_type, object_id):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(username=username, content_type=content_type, object_id=object_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        if not username:
            raise ValueError("Users must have an username")
        admin_user = AdminUser.objects.create(username=username)
        user = self.create_user(
            username=username,
            password=password,
            content_type=ContentType.objects.get_for_model(AdminUser),
            object_id=admin_user.id
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(
        ContentType, null=True, on_delete=models.SET_NULL
    )
    content_object = GenericForeignKey('content_type', 'object_id')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin_user(self):
        return isinstance(self.content_object, AdminUser)

    @property
    def is_organization_user(self):
        return isinstance(self.content_object, OrganizationUser)

    @property
    def is_end_user(self):
        return isinstance(self.content_object, EndUser)


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    space = models.IntegerField()
    user_limit = models.IntegerField()
    duration = models.IntegerField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    def clean(self):
        if self.space or self.user_limit or self.duration or self.price <= 0:
            raise ValidationError('My field must be greater than zero.')


class Subscription(models.Model):
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    organization = models.IntegerField()
    transaction_id = models.CharField(max_length=100)
    subscription_start = models.DateTimeField(default=datetime.datetime.now)
    subscription_end = models.DateTimeField(default=datetime.datetime.now)
    amount = models.FloatField()
    is_expired = models.BooleanField(default=False)
    referral_code = models.CharField(max_length=6, default='')


class OrganizationUser(models.Model):
    username = models.CharField(verbose_name="User email", max_length=200)
    company_name = models.CharField(max_length=40)
    company_contact_person = models.CharField(max_length=40)
    company_contact_no = models.CharField(max_length=40)
    company_address = models.CharField(max_length=40)
    company_state = models.CharField(max_length=40)
    company_city = models.CharField(max_length=40)
    company_description = models.CharField(max_length=100)
    company_logo_path = models.CharField(max_length=300, null=True)
    subscription_taken = models.BooleanField(default=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True)


class EndUser(models.Model):
    username = models.CharField(verbose_name="User mobile", max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50, null=True)
    encryption_key = models.CharField(max_length=100, default=generate_encryption_key)
    other_field_one = models.CharField(max_length=10000, default='{}')
    other_field_two = models.CharField(max_length=10000, default='{}')


class OrganizationsEndUser(models.Model):
    organization = models.ForeignKey(OrganizationUser, on_delete=models.CASCADE)
    enduser = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class UserOtp(models.Model):
    authuser = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    is_used = models.BooleanField(default=False)


class Notification(models.Model):
    organization = models.ForeignKey(OrganizationUser, on_delete=models.CASCADE)
    enduser = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    read_at = models.DateTimeField(default=datetime.datetime.now)
    is_read = models.BooleanField(default=False)


class Activity(models.Model):
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=20)
    action = models.CharField(max_length=200)
    ip = models.CharField(max_length=100)
    action_time = models.DateTimeField(default=datetime.datetime.now)


class Documents(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=300)
    file_name = models.CharField(max_length=300)
    size = models.FloatField()
    enduser = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(OrganizationUser, on_delete=models.CASCADE)
    added_time = models.DateTimeField(default=datetime.datetime.now)


class referralCode(models.Model):
    referral_code_name = models.CharField(max_length=6)
    referral_code_holder_name = models.CharField(max_length=50)
    percentage = models.FloatField()
    is_active = models.BooleanField(default=True)