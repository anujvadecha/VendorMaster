# Generated by Django 3.1.3 on 2020-12-20 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GlobalPremium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('buy_premium', models.FloatField(max_length=100)),
                ('sell_premium', models.FloatField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('vendor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('company', models.CharField(max_length=500)),
                ('gst_in', models.CharField(max_length=500)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('company_card_image', models.ImageField(blank=True, upload_to='')),
                ('company_logo', models.ImageField(blank=True, upload_to='')),
                ('margin_available', models.FloatField(blank=True, default=0, max_length=200)),
                ('pancard_photo', models.ImageField(blank=True, upload_to='')),
                ('promoter_name', models.CharField(blank=True, max_length=200)),
                ('reference_1', models.CharField(blank=True, max_length=500)),
                ('reference_2', models.CharField(blank=True, max_length=500)),
                ('default_margin', models.IntegerField(default=500)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VendorMargin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('margin', models.IntegerField(default=0)),
                ('margin_available', models.IntegerField(default=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendorbase.vendor')),
            ],
            options={
                'verbose_name': 'User margin',
                'verbose_name_plural': 'User margins',
            },
        ),
        migrations.CreateModel(
            name='VendorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('contact_details', models.TextField(blank=True)),
                ('office_address', models.TextField(blank=True)),
                ('collection_address', models.TextField(blank=True)),
                ('mobile_number_1', models.CharField(blank=True, max_length=13)),
                ('mobile_number_2', models.CharField(blank=True, max_length=13)),
                ('bank_details', models.TextField(blank=True)),
                ('gst_details', models.TextField(blank=True)),
                ('about_us', models.TextField(blank=True)),
                ('messages', models.TextField(blank=True)),
                ('delivery_charges', models.TextField(blank=True)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vendorbase.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('instrument_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('gold 999', 'gold 999'), ('gold 999 1kg', 'gold 999 1kg'), ('gold 995', 'gold 995'), ('gold 995 1kg', 'gold 995 1kg')], default='gold 999', max_length=200)),
                ('name', models.CharField(choices=[('gold 999', 'gold 999'), ('gold 999 1kg', 'gold 999 1kg'), ('gold 995', 'gold 995'), ('gold 995 1kg', 'gold 995 1kg'), ('gold 999 (T+1)', 'gold 999 t plus 1'), ('gold 999 1kg (T+1)', 'gold 999 1kg t plus 1'), ('gold 995 (T+1)', 'gold 995 t plus 1'), ('gold 995 1kg (T+1)', 'gold 995 1kg t plus 1'), ('gold 999 (T+2)', 'gold 999 t plus 2'), ('gold 999 1kg (T+2)', 'gold 999 1kg t plus 2'), ('gold 995 (T+2)', 'gold 995 t plus 2'), ('gold 995 1kg (T+2)', 'gold 995 1kg t plus 2')], max_length=500)),
                ('delivery_from', models.DateField()),
                ('delivery_to', models.DateField()),
                ('quantity', models.CharField(max_length=200)),
                ('source_symbol', models.CharField(choices=[('gold_fut', 'gold fut'), ('gold_bank', 'gold bank')], max_length=200)),
                ('buy_premium', models.FloatField()),
                ('sell_premium', models.FloatField()),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorbase.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('group_buy_premium', models.FloatField(max_length=100)),
                ('group_sell_premium', models.FloatField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('cities', models.ManyToManyField(to='vendorbase.City')),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorbase.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendorbase.symbol')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('bank_name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
                ('ifsc_code', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendorbase.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
