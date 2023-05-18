from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class productCards(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    image = models.ImageField(upload_to='main/static/main/img', verbose_name='Картинка')  # Поле для хранения картинки
    text = models.TextField(verbose_name='Описание')  # Поле для хранения текста
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  # Поле для хранения цены

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка товара'  # Название модели в единственном числе
        verbose_name_plural = 'Карточки товаров'  # Название модели во множественном числе




class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='main/static/main/img', verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка Слайдера'  # Название модели в единственном числе
        verbose_name_plural = 'Картинки Слайдера'  # Название модели во множественном числе


class TextIndex(models.Model):
    big_title = models.CharField(max_length=255, null=True,blank=True, verbose_name='Заголовок')
    big_text = models.TextField(verbose_name='Текст')
    LeftImg = models.BooleanField(default=False, verbose_name='Картинка слева')
    timage = models.ImageField(upload_to='main/static/main/textimg', null=True,blank=True, verbose_name='Картинка')
    Imagetitle = models.CharField(max_length=255, verbose_name='Подпись')

    class Meta:
        verbose_name = 'Текст Главной'  # Название модели в единственном числе
        verbose_name_plural = 'Тексты Главной'  # Название модели во множественном числе

    def __str__(self):
        words = self.big_text.split()  # Разделяем текст на слова
        first_three_words = ' '.join(words[:3]) + '...'  # Объединяем первые три слова в строку
        return first_three_words


class SubImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='main/static/main/subimg', verbose_name='Картинка')

    def clean(self):
        max_items = 2
        if SubImage.objects.count() >= max_items and not self.pk:
            raise ValidationError('Максимальное количество объектов: %d' % max_items)

    class Meta:
        verbose_name = 'Картинка возле слайдера'  # Название модели в единственном числе
        verbose_name_plural = 'Картинки возле слайдера'  # Название модели во множественном числе

    def __str__(self):
        return self.title



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
    email = models.EmailField(unique=True, verbose_name='Эл.Почта')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Администратор')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class appealUR(models.Model):
        UrFace = models.CharField(max_length=255, null=True, blank=True, verbose_name='Юр. Лицо')
        Fio = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО Руководителя')
        Phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='Телефон')
        address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')
        appeal = models.TextField(verbose_name='Обращение')

        class Meta:
            verbose_name = 'Обращение Юр. Лица'  # Название модели в единственном числе
            verbose_name_plural = 'Обращения Юр. Лиц'  # Название модели во множественном числе

        def __str__(self):
            words = self.appeal.split()  # Разделяем текст на слова
            appeal = ' '.join(words[:3]) + '...'  # Объединяем первые три слова в строку
            return appeal


class appealFIZ(models.Model):
        Fio = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО')
        Phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='Телефон')
        address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')
        appeal = models.TextField(verbose_name='Обращение')

        class Meta:
            verbose_name = 'Обращение Физ. Лица'  # Название модели в единственном числе
            verbose_name_plural = 'Обращения Физ. Лиц'  # Название модели во множественном числе

        def __str__(self):
            words = self.appeal.split()  # Разделяем текст на слова
            appeal = ' '.join(words[:3]) + '...'  # Объединяем первые три слова в строку
            return appeal