# Generated by Django 3.1.7 on 2021-04-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialog',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]