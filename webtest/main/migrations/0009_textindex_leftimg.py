# Generated by Django 4.1.7 on 2023-04-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_textindex_timage'),
    ]

    operations = [
        migrations.AddField(
            model_name='textindex',
            name='LeftImg',
            field=models.BooleanField(default=False),
        ),
    ]