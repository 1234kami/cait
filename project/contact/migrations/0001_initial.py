# Generated by Django 5.0 on 2023-12-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('location', models.CharField(blank=True, max_length=55, null=True, verbose_name='Местоположение')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронный адрес')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
