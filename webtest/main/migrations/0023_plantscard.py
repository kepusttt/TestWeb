# Generated by Django 4.2.1 on 2023-05-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_news_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantsCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='main/static/main/subimg', verbose_name='Картинка')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Продукция Растеиеводство',
                'verbose_name_plural': 'Продукция Растеиеводство',
            },
        ),
    ]
