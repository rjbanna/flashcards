# Generated by Django 2.2.4 on 2019-08-31 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carddecks', '0004_auto_20190831_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='users',
            new_name='user',
        ),
    ]