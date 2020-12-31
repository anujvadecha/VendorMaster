# Generated by Django 3.1.3 on 2020-12-31 04:55

from django.db import migrations, models
import orderManagement.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_id', models.CharField(blank=True, default=orderManagement.utils.unique_transaction_id_generator, editable=False, max_length=120)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(max_length=200)),
                ('type', models.CharField(choices=[('MARKET', 'MARKET'), ('LIMIT', 'LIMIT')], default='MARKET', max_length=200)),
                ('status', models.CharField(choices=[('OPEN', 'OPEN'), ('EXECUTED', 'EXECUTED'), ('CLOSED', 'CLOSED'), ('CANCELLED', 'CANCELLED'), ('WAITING_FOR_LIMIT', 'WAITING FOR LIMIT')], default='OPEN', max_length=100)),
                ('side', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], default='BUY', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
