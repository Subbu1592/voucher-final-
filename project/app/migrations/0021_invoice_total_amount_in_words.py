# Generated by Django 4.0.1 on 2023-01-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_invoice_course_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total_amount_in_words',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
