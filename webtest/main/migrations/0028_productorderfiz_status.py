# Generated by Django 4.2 on 2023-05-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_productorderur_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorderfiz',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]
