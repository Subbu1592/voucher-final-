# Generated by Django 4.0.1 on 2023-01-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_voucher_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='gst_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
