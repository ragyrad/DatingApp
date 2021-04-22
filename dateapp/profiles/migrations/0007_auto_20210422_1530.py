# Generated by Django 3.1.7 on 2021-04-22 15:30

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210422_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='country', chained_model_field='country', null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.country'),
        ),
    ]
