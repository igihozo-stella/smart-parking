# Generated by Django 3.1.7 on 2021-02-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0007_auto_20210220_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='username',
        ),
    ]