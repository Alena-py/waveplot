# Generated by Django 2.2.6 on 2020-09-20 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='title',
        ),
    ]