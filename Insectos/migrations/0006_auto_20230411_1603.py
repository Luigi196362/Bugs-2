# Generated by Django 3.1.3 on 2023-04-11 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insectos', '0005_auto_20230411_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insecto',
            old_name='nomcientifico',
            new_name='nombrecientifico',
        ),
    ]
