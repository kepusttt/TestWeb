# Generated by Django 4.2 on 2023-05-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_productcards_name_productcards_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Картинка Слайдера', 'verbose_name_plural': 'Картинки Слайдера'},
        ),
        migrations.AlterModelOptions(
            name='productcards',
            options={'verbose_name': 'Карточка товара', 'verbose_name_plural': 'Карточки товаров'},
        ),
        migrations.AlterModelOptions(
            name='subimage',
            options={'verbose_name': 'Картинка возле слайдера', 'verbose_name_plural': 'Картинки возле слайдера'},
        ),
        migrations.AlterModelOptions(
            name='textindex',
            options={'verbose_name': 'Текст Главной', 'verbose_name_plural': 'Тексты Главной'},
        ),
        migrations.AddField(
            model_name='textindex',
            name='Imagetitle',
            field=models.CharField(default=1, max_length=255, verbose_name='Подпись'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Эл.Почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='main/static/main/img', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productcards',
            name='image',
            field=models.ImageField(upload_to='main/static/main/img', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='productcards',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='productcards',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='productcards',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='subimage',
            name='image',
            field=models.ImageField(upload_to='main/static/main/subimg', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='subimage',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='textindex',
            name='LeftImg',
            field=models.BooleanField(default=False, verbose_name='Картинка слева'),
        ),
        migrations.AlterField(
            model_name='textindex',
            name='big_text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='textindex',
            name='big_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='textindex',
            name='timage',
            field=models.ImageField(blank=True, null=True, upload_to='main/static/main/textimg', verbose_name='Картинка'),
        ),
    ]
