# Generated by Django 4.2.16 on 2024-09-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_subcategorymodel_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='songmodel',
            name='trans_Id',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]
