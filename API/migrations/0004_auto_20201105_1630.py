# Generated by Django 3.1.2 on 2020-11-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20201105_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='distance_from_sun',
            field=models.IntegerField(),
        ),
    ]
