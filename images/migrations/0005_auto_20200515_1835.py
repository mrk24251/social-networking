# Generated by Django 2.2.3 on 2020-05-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_comment_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
