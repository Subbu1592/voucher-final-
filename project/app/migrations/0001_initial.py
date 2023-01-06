# Generated by Django 4.0.1 on 2022-12-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_to', models.CharField(max_length=100)),
                ('invoice_no', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(auto_now_add=True)),
                ('gst_no', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.CharField(max_length=100)),
                ('unit_price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('due_date1', models.DateField()),
                ('due_date2', models.DateField()),
                ('due_date3', models.DateField()),
            ],
        ),
    ]
