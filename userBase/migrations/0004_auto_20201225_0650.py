# Generated by Django 3.1.3 on 2020-12-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBase', '0003_normaluser_is_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='business_card',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='gst_in_no',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='reference_1_mobile',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='reference_1_name',
            field=models.CharField(blank=True, help_text='Please input name and number of any reference we can verify', max_length=200),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='reference_2_name',
            field=models.CharField(blank=True, help_text='Please input name and number of any reference we can verify', max_length=200),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='reference_3_mobile',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='requested_registration',
            field=models.BooleanField(default=False),
        ),
    ]
