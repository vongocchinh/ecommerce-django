# Generated by Django 3.1.7 on 2021-06-10 02:11

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0044_auto_20210610_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2, verbose_name='country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='zip',
            field=models.CharField(blank=True, max_length=5, verbose_name='zipcode'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=2),
        ),
    ]