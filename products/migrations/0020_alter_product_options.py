# Generated by Django 3.2.19 on 2023-09-14 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
    ]
