# Generated by Django 2.2.4 on 2019-09-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carddecks', '0008_auto_20190901_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deck_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
