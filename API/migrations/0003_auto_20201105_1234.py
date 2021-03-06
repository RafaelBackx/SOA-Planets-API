# Generated by Django 3.1.2 on 2020-11-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='planet',
            old_name='radius',
            new_name='diameter',
        ),
        migrations.AddField(
            model_name='planet',
            name='atmosphere_main_components',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='distance_from_sun',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='moons',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='period_of_revolution',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='rings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='rotation_speed',
            field=models.CharField(default='None', max_length=60),
            preserve_default=False,
        ),
    ]
