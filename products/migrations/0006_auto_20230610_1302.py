# Generated by Django 3.2.19 on 2023-06-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='display_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='display_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='display_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('lotion', 'Lotion'), ('spray', 'Spray'), ('stick', 'Stick'), ('roll-on', 'Roll-On')], max_length=30),
        ),
    ]