# Generated by Django 3.1.3 on 2020-12-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBase', '0002_auto_20201223_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
