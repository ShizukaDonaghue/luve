# Generated by Django 3.2.19 on 2023-06-10 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_brand_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='display_name',
        ),
        migrations.RemoveField(
            model_name='type',
            name='display_name',
        ),
    ]
