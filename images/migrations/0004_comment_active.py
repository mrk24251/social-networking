# Generated by Django 2.2.3 on 2020-04-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
