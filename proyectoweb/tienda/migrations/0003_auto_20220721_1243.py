# Generated by Django 3.0.4 on 2022-07-21 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20220721_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriaprod',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='update',
            new_name='updated',
        ),
    ]
