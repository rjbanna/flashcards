# Generated by Django 2.2.4 on 2019-08-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('is_active', models.IntegerField()),
                ('activation_code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
