# Generated by Django 3.1.7 on 2021-05-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210517_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'SportWear'), ('Ow', 'OutWear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='test description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('D', 'danger'), ('P', 'primary')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]
