# Generated by Django 3.2.19 on 2023-09-03 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
    ]
