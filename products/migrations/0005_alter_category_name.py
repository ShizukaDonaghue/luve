# Generated by Django 3.2.19 on 2023-06-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230609_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('baby_kids', 'Baby & Kids'), ('body', 'Body'), ('face', 'Face'), ('lips', 'Lips'), ('after_sun', 'After Sun')], max_length=30),
        ),
    ]
