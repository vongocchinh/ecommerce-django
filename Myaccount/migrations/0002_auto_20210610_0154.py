# Generated by Django 3.1.7 on 2021-06-09 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myaccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mod_date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='telephone',
        ),
    ]