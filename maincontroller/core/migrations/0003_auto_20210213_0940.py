# Generated by Django 3.1.6 on 2021-02-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210213_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Айди города')),
                ('city_name', models.TextField(verbose_name='Город')),
            ],
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'managed': False, 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='clientwork',
            options={'managed': False, 'verbose_name': 'Клиент - работа', 'verbose_name_plural': 'Клиенты - работы'},
        ),
        migrations.AlterModelOptions(
            name='clientworkpreferences',
            options={'managed': False, 'verbose_name': 'Избранные категории клиента', 'verbose_name_plural': 'Избранные категории клиентов'},
        ),
        migrations.AlterModelOptions(
            name='scrapper',
            options={'managed': False, 'verbose_name': 'Парсер', 'verbose_name_plural': 'Парсеры'},
        ),
    ]
