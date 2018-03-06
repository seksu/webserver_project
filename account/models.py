from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission)
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.utils import timezone, six
from camera.models import Company
from django.utils.translation import ugettext_lazy as _


class AccountManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The given email must be set'))
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email=email,
                                 password=password,
                                 **extra_fields)

    def create_superuser(self, email, password):
        user = self._create_user(email=email,
                                 password=password)
        user.is_admin = True
        user.role = 1
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        (1, 'SuperAdmin'),
        (2, 'UserAdmin'),
        (3, 'UserEmployee')
    )

    email = models.EmailField(max_length=255, unique=True)
    facepath = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)

    role = models.SmallIntegerField(choices=ROLE_CHOICES, default=0)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    last_active = models.DateTimeField(_('last active'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
