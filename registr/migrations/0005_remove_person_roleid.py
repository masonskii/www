# Generated by Django 4.0.2 on 2022-02-21 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registr', '0004_remove_person_lastentrance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='roleId',
        ),
    ]
