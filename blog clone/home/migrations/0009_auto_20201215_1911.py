# Generated by Django 3.1.4 on 2020-12-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201215_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='title_name',
            field=models.CharField(default='No Title', max_length=264),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='url_field',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='discoverbookmark',
            name='url_field',
            field=models.URLField(unique=True),
        ),
    ]
