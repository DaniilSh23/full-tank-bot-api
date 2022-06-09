from rest_framework import serializers

from bot_api.models import Categories, Items, MediaForItems, OrderBasket, Order


class CategoriesSerializer(serializers.ModelSerializer):
    '''Сериалайзер для категорий товаров'''

    class Meta:
        model = Categories
        fields = ['id', 'category_name']


class ItemsSerializer(serializers.ModelSerializer):
    '''Сериалайзер для товаров'''

    class Meta:
        model = Items
        fields = '__all__'


class OrderBasketSerializer(serializers.ModelSerializer):
    '''Сериалайзер для товаров из корзины'''

    class Meta:
        model = OrderBasket
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    '''Сериалайзер для заказов'''

    class Meta:
        model = Order
        fields = ['pk', 'user_tlg_id', 'datetime', 'pay_status', 'execution_status', 'order_items', 'result_orders_price']
