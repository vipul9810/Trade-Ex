# Generated by Django 2.1.2 on 2018-11-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20181122_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='isSeller',
        ),
    ]