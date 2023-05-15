# Generated by Django 4.2 on 2023-05-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='productCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main/static/main/img')),
                ('text', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
