# Generated by Django 2.2.3 on 2020-06-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0018_auto_20200607_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=200),
        ),
    ]