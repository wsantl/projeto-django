# Generated by Django 5.1.3 on 2024-11-11 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoa',
            new_name='User',
        ),
    ]