# Generated by Django 3.1.7 on 2021-04-29 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210428_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='dialog',
        ),
        migrations.DeleteModel(
            name='Dialog',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
