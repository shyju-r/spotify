# Generated by Django 4.2.5 on 2024-08-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_songmodel_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='internationalmixes',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='madeforyou',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='malayalam',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='tamil',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='topmixes',
        ),
    ]