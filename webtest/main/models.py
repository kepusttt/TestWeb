from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main/static/main/img')

    def __str__(self):
        return self.title


class TextIndex(models.Model):
    big_title = models.CharField(max_length=255, null=True,blank=True)
    big_text = models.TextField()
    LeftImg = models.BooleanField(default=False)
    timage = models.ImageField(upload_to='main/static/main/textimg', null=True,blank=True)


class SubImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main/static/main/subimg')

    def clean(self):
        max_items = 2
        if SubImage.objects.count() >= max_items and not self.pk:
            raise ValidationError('Максимальное количество объектов: %d' % max_items)



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email