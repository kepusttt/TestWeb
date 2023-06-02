# Generated by Django 4.2 on 2023-05-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_animalssi_chillsi_plantssi_tradesi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalsText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текст Животноводства',
                'verbose_name_plural': 'Тексты Животноводства',
            },
        ),
        migrations.CreateModel(
            name='ChillText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текст Отдыха',
                'verbose_name_plural': 'Тексты Отдыха',
            },
        ),
        migrations.CreateModel(
            name='PlantsText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текст Растениеводства',
                'verbose_name_plural': 'Тексты Растениеводства',
            },
        ),
        migrations.CreateModel(
            name='TradeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Текст Торговли',
                'verbose_name_plural': 'Тексты Торговли',
            },
        ),
    ]