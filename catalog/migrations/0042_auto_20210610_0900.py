# Generated by Django 3.1.7 on 2021-06-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0041_auto_20210610_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='checkout_date',
        ),
        migrations.AddField(
            model_name='bill',
            name='address',
            field=models.CharField(blank=True, max_length=50, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=2),
        ),
    ]