# Generated by Django 3.2.19 on 2023-06-10 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20230610_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='display_name',
        ),
    ]
