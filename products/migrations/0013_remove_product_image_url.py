# Generated by Django 3.2.19 on 2023-06-15 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
