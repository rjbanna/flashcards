# Generated by Django 2.2.4 on 2019-08-31 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_password_reset_code'),
        ('carddecks', '0002_auto_20190831_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='users',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
