from rest_framework import serializers

from bot_api.models import Categories, Items, MediaForItems, OrderBasket, Order, PaidOrder, OrderArchive


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


class PaidOrderSerializer(serializers.ModelSerializer):
    '''Сериалайзер для данных об оплате заказа.'''

    class Meta:
        model = PaidOrder
        fields = '__all__'


class OrderArchiveSerializer(serializers.ModelSerializer):
    '''Сериалайзер для архива заказов'''

    class Meta:
        model = OrderArchive
        fields = '__all__'
