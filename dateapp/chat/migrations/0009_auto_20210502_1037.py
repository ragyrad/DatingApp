# Generated by Django 3.1.7 on 2021-05-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20210502_1035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['timestamp']},
        ),
    ]