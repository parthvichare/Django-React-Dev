# Generated by Django 5.0.6 on 2024-06-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_name_post_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='beds',
            field=models.IntegerField(null=True),
        ),
    ]