# Generated by Django 4.0.4 on 2022-06-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0016_alter_order_order_items_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_tlg_id', models.CharField(db_index=True, max_length=50, verbose_name='ID телеграма пользователя')),
                ('user_tlg_name', models.CharField(max_length=100, verbose_name='Имя пользователя в телеграме')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'Пользователи',
                'ordering': ['id'],
            },
        ),
    ]
