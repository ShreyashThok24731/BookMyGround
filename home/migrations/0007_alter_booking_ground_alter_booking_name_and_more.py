# Generated by Django 4.2.1 on 2023-06-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ground',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
