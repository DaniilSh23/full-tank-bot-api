# Generated by Django 4.0.4 on 2022-06-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0008_alter_items_image_for_items_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='execution_status',
            field=models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Статус выполнения заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_status',
            field=models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Статус оплаты'),
        ),
    ]