# Generated by Django 2.0.2 on 2018-03-03 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='lon',
            new_name='lng',
        ),
    ]
