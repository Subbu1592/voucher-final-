# Generated by Django 4.0.1 on 2023-01-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_delete_invoice_voucher_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='payment_mode',
            field=models.CharField(blank=True, choices=[('card', 'card'), ('cash', 'cash'), ('digital pay', 'digital pay')], max_length=100, null=True),
        ),
    ]
