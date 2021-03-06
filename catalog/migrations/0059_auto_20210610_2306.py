# Generated by Django 3.1.7 on 2021-06-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0058_auto_20210610_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='checkout_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=2),
        ),
    ]
