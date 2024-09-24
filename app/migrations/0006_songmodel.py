# Generated by Django 4.2.5 on 2024-08-14 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_categorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(null=True)),
                ('playlistimage', models.ImageField(null=True, upload_to='images')),
                ('playlistname', models.TextField(null=True)),
                ('playlistartists', models.TextField(null=True)),
                ('number', models.TextField(null=True)),
                ('songimage', models.ImageField(null=True, upload_to='images')),
                ('songname', models.TextField(null=True)),
                ('songartist', models.TextField(null=True)),
                ('moviename', models.TextField(null=True)),
                ('plays', models.TextField(null=True)),
                ('duration', models.TextField(null=True)),
            ],
        ),
    ]
