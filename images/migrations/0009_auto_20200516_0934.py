# Generated by Django 2.2.3 on 2020-05-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_auto_20200515_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(),
        ),
    ]