# Generated by Django 4.1.7 on 2023-04-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_bigtitle_textindex_big_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textindex',
            name='big_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
