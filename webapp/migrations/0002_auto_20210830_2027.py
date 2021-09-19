# Generated by Django 3.2.5 on 2021-08-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.IntegerField()),
                ('Product_name', models.CharField(max_length=25)),
                ('Product_price', models.IntegerField()),
                ('Product_manufacturer', models.CharField(max_length=30)),
                ('Product_image', models.ImageField(blank=True, null=True, upload_to='dbimages/')),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Mailid', models.CharField(max_length=60)),
                ('contactnumber', models.BigIntegerField()),
                ('Location', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
