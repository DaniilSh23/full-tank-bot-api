# Generated by Django 4.0.4 on 2022-06-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0003_items_image_for_items_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbasket',
            name='items_number_in_basket',
            field=models.IntegerField(null=True, verbose_name='Количество данного товара в корзине'),
        ),
    ]
