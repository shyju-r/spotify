# Generated by Django 4.2.5 on 2024-08-28 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_subcategorymodel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songmodel',
            name='category',
        ),
    ]
