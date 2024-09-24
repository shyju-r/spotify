# Generated by Django 4.2.5 on 2024-08-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_songmodel_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='songmodel',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='songmodel',
            name='song',
            field=models.FileField(null=True, upload_to='audio_files/'),
        ),
    ]