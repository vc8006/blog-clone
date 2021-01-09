# Generated by Django 3.1.4 on 2020-12-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201215_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discoverbookmark',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
