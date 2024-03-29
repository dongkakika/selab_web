from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, userid, password, username, email, activate, auth, **extra_fields):
        user = self.model(
            userid=userid,
            username=username,
            email=email,
            activate=activate,
            auth=auth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, password, username=None, email=None, activate=False, auth=None):
        user = self.create_user(userid, password, username, email, activate, auth)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.level = 0
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    userid = models.CharField(max_length=20, verbose_name="ID", unique=True)
    password = models.CharField(max_length=256, verbose_name="PW")
    email = models.EmailField(max_length=128, verbose_name="email", null=True, unique=True)
    username = models.CharField(max_length=50, verbose_name="username", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="level", default=3)
    auth = models.CharField(max_length=10, verbose_name="auth", null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date_joined', null=True, blank=True)
    activate = models.BooleanField(default=False, verbose_name='activate')

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.userid

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "user"