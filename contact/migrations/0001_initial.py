# Generated by Django 3.2.19 on 2023-09-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(choices=[('', 'Query Type *'), ('Product Query', 'Product Query'), ('Order Query', 'Order Query'), ('Returns', 'Returns'), ('Other', 'Other')], max_length=50)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
