# Generated by Django 4.0.1 on 2023-01-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_voucher_card_details_voucher_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='on_account_of',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
