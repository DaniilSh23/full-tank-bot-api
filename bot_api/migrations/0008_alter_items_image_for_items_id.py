# Generated by Django 4.0.4 on 2022-06-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0007_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image_for_items_id',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='ID картинки для товара'),
        ),
    ]