# Generated by Django 3.1.7 on 2021-05-18 01:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20210512_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='max_age_looking_for',
            field=models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='min_age_looking_for',
            field=models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
