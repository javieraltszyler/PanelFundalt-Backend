from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class User(AbstractUser):
    pass
#     """
#     Custom user model that extends Django's AbstractUser.
#     Adds additional fields and functionality specific to our application.
#     """
#     email = models.EmailField(
#         _('email address'),
#         unique=True,
#         help_text=_('Required. Enter a valid email address.')
#     )
#     phone_regex = RegexValidator(
#         regex=r'^\+?1?\d{9,15}$',
#         message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     )
#     phone = models.CharField(
#         _('phone number'),
#         validators=[phone_regex],
#         max_length=17,
#         blank=True,
#         help_text=_('Optional. Enter a valid phone number.')
#     )
#     dni = models.CharField(
#         _('DNI'),
#         max_length=20,
#         unique=True,
#         help_text=_('Required. Enter a valid DNI number.')
#     )
#     is_verified = models.BooleanField(
#         _('verified'),
#         default=False,
#         help_text=_('Designates whether this user has verified their email address.')
#     )
#     last_login_ip = models.GenericIPAddressField(
#         _('last login IP'),
#         null=True,
#         blank=True,
#         help_text=_('IP address of the user\'s last login.')
#     )
#     created_at = models.DateTimeField(
#         _('created at'),
#         auto_now_add=True
#     )
#     updated_at = models.DateTimeField(
#         _('updated at'),
#         auto_now=True
#     )

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#         ordering = ['-date_joined']

#     def __str__(self):
#         return f"{self.get_full_name()} ({self.email})"

#     def get_full_name(self):
#         """
#         Return the user's full name, or email if name is not set.
#         """
#         full_name = f"{self.first_name} {self.last_name}".strip()
#         return full_name if full_name else self.email

#     def get_short_name(self):
#         """
#         Return the user's first name, or email if first name is not set.
#         """
#         return self.first_name if self.first_name else self.email



# class User(models.Model):
#     organization = models.ForeignKey(
#         'organization',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="users",
#         verbose_name="organization"
#     )
#     email = models.EmailField(
#         unique=True,
#         verbose_name="email"
#     )
#     password = models.CharField(
#         max_length=255,
#         verbose_name="password"
#     )
#     first_name = models.CharField(
#         max_length=50,
#         verbose_name="first name"
#     )
#     last_name = models.CharField(
#         max_length=50,
#         verbose_name="last name"
#     )
#     phone = models.CharField(
#         max_length=20,
#         blank=True,
#         null=True,
#         verbose_name="phone"
#     )
#     is_active = models.BooleanField(
#         default=True,
#         verbose_name="active"
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="created at"
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#         verbose_name="updated at"
#     )


#     class Meta:
#         db_table = 'users'
