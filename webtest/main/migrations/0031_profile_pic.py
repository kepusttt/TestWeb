# Generated by Django 4.2 on 2023-06-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default=1, upload_to='main/static/main/subimg'),
            preserve_default=False,
        ),
    ]