# Generated by Django 4.0.2 on 2022-03-09 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_furnitures_dimension_furnitures_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furnitures',
            name='dimension',
        ),
        migrations.RemoveField(
            model_name='furnitures',
            name='price',
        ),
        migrations.RemoveField(
            model_name='furnitures',
            name='stock',
        ),
    ]
