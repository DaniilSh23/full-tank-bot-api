# Generated by Django 4.0.4 on 2022-06-09 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0011_paidorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidorder',
            name='customer_name',
            field=models.CharField(default=None, max_length=50, verbose_name='Имя клиента'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidorder',
            name='customer_telephone_number',
            field=models.CharField(default=None, max_length=20, verbose_name='Телефон клиента'),
            preserve_default=False,
        ),
    ]
