# Generated by Django 3.2.5 on 2021-08-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
