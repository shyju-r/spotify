# Generated by Django 4.2.5 on 2024-08-26 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_songmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songmodel',
            name='song',
        ),
    ]