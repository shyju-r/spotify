# Generated by Django 4.2.5 on 2024-08-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_categorymodel_internationalmixes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategorymodel',
            name='category',
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='category_name',
            field=models.TextField(null=True),
        ),
    ]