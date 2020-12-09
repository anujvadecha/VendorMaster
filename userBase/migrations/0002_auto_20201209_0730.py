# Generated by Django 3.1.3 on 2020-12-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
