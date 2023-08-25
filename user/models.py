from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    
    Users models using UserManager
    
    """
    # id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4)
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    """

        USERNAME_FIELD - это атрибут модели, \
        который указvывает, какое поле будет использоваться для аутентификации пользователя по умолчанию. 

    """
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        'email',
        'password'
    ]

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'

    def __str__(self) -> str:
        return self.username


class Phone(models.Model):
    phone = PhoneNumberField(unique=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)


class WalletFill(models.Model):
    money_up = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.money_up)


class WalletReduction(models.Model):
    money_down = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.money_down)

