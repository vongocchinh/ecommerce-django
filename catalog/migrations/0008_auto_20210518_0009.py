# Generated by Django 3.1.7 on 2021-05-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210518_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('Ow', 'OutWear'), ('SW', 'SportWear')], max_length=2),
        ),
    ]
