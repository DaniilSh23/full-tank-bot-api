# Generated by Django 4.0.4 on 2022-06-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0009_alter_order_execution_status_alter_order_pay_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id_before_receiving', models.IntegerField(verbose_name='ID заказа перед получением клиентом')),
                ('user_tlg_id', models.CharField(max_length=20, verbose_name='ID пользователя телеграм')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')),
                ('pay_status', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Статус оплаты')),
                ('execution_status', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Статус выполнения заказа')),
                ('order_items', models.TextField(max_length=4000, verbose_name='Товары из заказа')),
                ('result_orders_price', models.FloatField(verbose_name='Итоговая цена заказа')),
            ],
            options={
                'verbose_name': 'Архив заказа',
                'verbose_name_plural': 'Архив заказов',
                'db_table': 'Архив заказов',
                'ordering': ['-datetime'],
            },
        ),
    ]
