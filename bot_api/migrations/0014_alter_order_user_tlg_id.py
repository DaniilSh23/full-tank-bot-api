# Generated by Django 4.0.4 on 2022-06-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0013_alter_orderarchive_user_tlg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_tlg_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ID пользователя телеграм'),
        ),
    ]