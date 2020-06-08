from django_mongoengine import fields,Document
from datetime import datetime
import os
from django_mongoengine.mongo_auth.models import AbstractBaseUser#, BaseUserManager

'''
class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.Document(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user
'''
class User(AbstractBaseUser):
    email = fields.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = fields.StringField(max_length=50,unique=True)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)
    is_admin = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    #objects= UserManager()

    def __str__(self):
        return self.username



'''
from django_mongoengine import fields
from datetime import datetime
import os
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class custom_user(AbstractBaseUser):
    email = fields.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = fields.StringField(max_length=50,unique=True)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)
    is_admin = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        return True
'''
