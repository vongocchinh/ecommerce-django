# Generated by Django 3.1.7 on 2021-06-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myaccount', '0003_remove_userprofile_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Last modified'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='org',
            field=models.CharField(blank=True, max_length=128, verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Telephone'),
        ),
    ]