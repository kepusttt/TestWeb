from django.db import models
from django.core.exceptions import ValidationError

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