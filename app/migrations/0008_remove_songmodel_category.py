# Generated by Django 4.2.5 on 2024-08-26 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_songmodel_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songmodel',
            name='category',
        ),
    ]
