# Generated by Django 3.2.5 on 2021-09-07 14:55

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_account'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
