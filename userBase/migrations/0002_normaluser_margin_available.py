# Generated by Django 3.1.3 on 2020-12-05 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='margin_available',
            field=models.FloatField(blank=True, default=0, max_length=200),
        ),
    ]
