# Generated by Django 3.2.6 on 2021-10-17 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='question',
            new_name='Name',
        ),
    ]
