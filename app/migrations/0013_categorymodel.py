# Generated by Django 4.2.5 on 2024-08-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_songmodel_category_songmodel_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('madeforyou', models.TextField()),
                ('topmixes', models.TextField()),
                ('tamil', models.TextField()),
                ('malayalam', models.TextField()),
                ('internationalmixes', models.TextField()),
            ],
        ),
    ]
