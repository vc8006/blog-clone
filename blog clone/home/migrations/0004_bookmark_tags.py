# Generated by Django 3.1.4 on 2020-12-12 10:44

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('home', '0003_auto_20201209_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
