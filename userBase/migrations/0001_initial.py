# Generated by Django 3.1.3 on 2020-11-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(null=True)),
                ('user_type', models.CharField(choices=[('USER', 'user'), ('VENDOR', 'vendor')], max_length=200, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
