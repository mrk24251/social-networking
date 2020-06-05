# Generated by Django 2.2.3 on 2020-06-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20200516_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='filter',
            field=models.CharField(default='Normal', max_length=60),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(),
        ),
    ]