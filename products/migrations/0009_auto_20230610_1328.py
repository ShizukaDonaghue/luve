# Generated by Django 3.2.19 on 2023-06-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230610_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Baby & Kids', 'Baby & Kids'), ('Body', 'Body'), ('Face', 'Face'), ('Lips', 'Lips'), ('After Sun', 'After Sun')], max_length=30),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('Lotion', 'Lotion'), ('Spray', 'Spray'), ('Stick', 'Stick'), ('Roll-On', 'Roll-On')], max_length=30),
        ),
    ]