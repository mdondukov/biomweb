# Generated by Django 2.1.5 on 2019-01-25 20:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter the page content'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content_en',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter the page content', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='content_ru',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter the page content', null=True),
        ),
    ]