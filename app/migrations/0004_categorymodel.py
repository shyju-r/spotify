# Generated by Django 4.2.5 on 2024-08-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('madeforyou', models.TextField(null=True)),
                ('yourtopmixes', models.TextField(null=True)),
                ('tamil', models.TextField(null=True)),
                ('malayalam', models.TextField(null=True)),
                ('internationalmixes', models.TextField(null=True)),
            ],
        ),
    ]