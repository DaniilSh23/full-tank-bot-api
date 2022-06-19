from django.db import models


class Categories(models.Model):
    '''Модель для категорий товаров'''
    category_name = models.CharField(max_length=50, verbose_name='Название категории товаров')

    class Meta:
        ordering = ['id']
        db_table = 'Категории товаров'
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.category_name


class Items(models.Model):
    '''Модель для товаров'''
    items_name = models.CharField(max_length=50, verbose_name='Название товара')
    description = models.TextField(max_length=2000, verbose_name='Описание товара')
    price = models.FloatField(max_length=10, verbose_name='Цена товара')
    number_of_items = models.IntegerField(verbose_name='Количество товара в наличии')
    items_category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория товаров')
    image_for_items_id = models.TextField(max_length=2000, verbose_name='ID картинки для товара', null=True, blank=True)

    class Meta:
        ordering = ['price']
        db_table = 'Товары'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.items_name


class MediaForItems(models.Model):
    '''Медиа файлы(картинки) для товаров'''
    for_item = models.ForeignKey(to=Items, on_delete=models.CASCADE, verbose_name='Для товара', null=True, blank=True)
    file_path = models.FileField(upload_to=f'files/%Y/%m/%d', max_length=5000, null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'Медиа для товаров'
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class OrderBasket(models.Model):
    '''Модель для корзины заказа'''
    items_id = models.ForeignKey(to=Items, on_delete=models.CASCADE, verbose_name='ID товара')
    items_number_in_basket = models.IntegerField(verbose_name='Количество данного товара в корзине', default=1)
    user_tlg_id = models.CharField(max_length=20, verbose_name='ID пользователя телеграм')

    class Meta:
        ordering = ['id']
        db_table = 'Товары в корзине'
        verbose_name = 'Товары в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return self.user_tlg_id


class Order(models.Model):
    '''Модель для заказа'''

    user_tlg_id = models.CharField(max_length=20, verbose_name='ID пользователя телеграм')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    pay_status = models.BooleanField(default=False, verbose_name='Статус оплаты', db_index=True, null=True, blank=True)
    execution_status = models.BooleanField(default=False, verbose_name='Статус выполнения заказа', db_index=True, null=True, blank=True)
    order_items = models.TextField(max_length=4000, verbose_name='Товары из заказа')
    result_orders_price = models.FloatField(verbose_name='Итоговая цена заказа')

    class Meta:
        ordering = ['-datetime']
        db_table = 'Заказы'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.user_tlg_id


class OrderArchive(models.Model):
    '''Модель для архива заказов, которые были: оплачены --> выполнены --> получены.'''

    order_id_before_receiving = models.IntegerField(verbose_name='ID заказа перед получением клиентом')
    user_tlg_id = models.CharField(max_length=20, verbose_name='ID пользователя телеграм')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    pay_status = models.BooleanField(default=False, verbose_name='Статус оплаты', db_index=True, null=True, blank=True)
    execution_status = models.BooleanField(default=False, verbose_name='Статус выполнения заказа', db_index=True, null=True, blank=True)
    order_items = models.TextField(max_length=4000, verbose_name='Товары из заказа')
    result_orders_price = models.FloatField(verbose_name='Итоговая цена заказа')

    class Meta:
        ordering = ['-datetime']
        db_table = 'Архив заказов'
        verbose_name = 'Архив заказа'
        verbose_name_plural = 'Архив заказов'

    def __str__(self):
        return self.user_tlg_id


class PaidOrder(models.Model):
    '''Модель для данных об оплате заказа.'''

    order_id = models.CharField(verbose_name='номер заказа', max_length=50)
    total_price = models.FloatField(verbose_name='Итоговая сумма заказа')
    tlg_payment_charge_id = models.CharField(verbose_name='ID списания(телеграм)', max_length=200)
    provider_payment_charge_id = models.CharField(verbose_name='ID списания(банк)', max_length=200)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    customer_name = models.CharField(verbose_name='Имя клиента', max_length=50)
    customer_telephone_number = models.CharField(verbose_name='Телефон клиента', max_length=20)

    class Meta:
        ordering = ['-datetime']
        db_table = 'Данные об оплате заказов'
        verbose_name = 'Данные об оплате заказов'
        verbose_name_plural = 'Данные об оплате заказов'


class BotUsers(models.Model):
    '''Пользователи бота'''

    user_tlg_id = models.CharField(verbose_name='ID телеграма пользователя', max_length=50, db_index=True)
    user_tlg_name = models.CharField(verbose_name='Имя пользователя в телеграме', max_length=100)

    class Meta:
        ordering = ['id']
        db_table = 'Пользователи'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user_tlg_id



