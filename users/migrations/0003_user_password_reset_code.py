# Generated by Django 2.2.4 on 2019-08-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190829_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_reset_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]