# Generated by Django 3.1.3 on 2023-04-11 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insectos', '0006_auto_20230411_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insecto',
            old_name='nombrecientifico',
            new_name='nomcientifico',
        ),
    ]
