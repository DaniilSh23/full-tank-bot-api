from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from bot_api.models import Categories, Items, OrderBasket, Order
from bot_api.serializers import ItemsSerializer, CategoriesSerializer, OrderBasketSerializer, OrderSerializer


# 1
class CategoryView(generics.ListAPIView):
    '''Представление списка всех категорий'''

    serializer_class = CategoriesSerializer
    # выбор класса-пагинатора
    pagination_class = PageNumberPagination     # кажется, его не обязательно прописывать

    def get_queryset(self):
        '''
        Переопределённый метод из GenericAPIView для отбора нужных нам данных
        '''
        # берём все данные из таблицы БД
        queryset = Categories.objects.all()
        return queryset


# 2
class ItemsListView(generics.ListAPIView):
    '''Представление списка всех товаров для конкретной категории'''

    serializer_class = ItemsSerializer
    # выбор класса-пагинатора
    pagination_class = PageNumberPagination     # кажется, его не обязательно прописывать

    def get_queryset(self):
        '''
        Переопределённый метод из GenericAPIView для отбора нужных нам данных
        '''

        # берём данные по ключу items_category из запроса пользователя
        items_category_id = self.request.query_params.get('items_category_id')
        # проверяем есть ли данные по такому ключу в запросе пользователя
        if items_category_id:
            # отбираем те записи БД, у которых поле items_category == значению из запроса пользователя
            queryset = Items.objects.filter(items_category=items_category_id)
        else:
            queryset = Items.objects.all()
        return queryset


# 3
class OrderBasketView(APIView):
    '''Представление списка товаров из корзины пользователя.
    В запросе требуется укзать /?user_tlg_id=...
    И при необходимости получить конкретный товар ...&items_id='''

    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        user_tlg_id = request.query_params.get('user_tlg_id')
        items_id = request.query_params.get('items_id')
        if items_id:
            user_basket = OrderBasket.objects.filter(user_tlg_id=user_tlg_id, items_id__pk=items_id).select_related('items_id')
        else:
            user_basket = OrderBasket.objects.filter(user_tlg_id=user_tlg_id).select_related('items_id')
        user_basket = user_basket.values_list(
                'items_id',
                'items_id__items_name',
                'items_id__price',
                'items_number_in_basket',
                'items_id__number_of_items',
            )
        return Response(user_basket, status.HTTP_200_OK)


# 4
class AddItemToBasket(APIView):
    '''Представление для добавления товара в корзину'''

    def get(self, request, format=None):
        # получение параметров запроса
        user_tlg_id = request.query_params.get('user_tlg_id')
        item_id = request.query_params.get('item_id')

        # берём объект товара
        item = Items.objects.get(pk=item_id)
        if item.number_of_items != 0:
            item.number_of_items -= 1
            item.save()
        else:
            return Response({'no_items': 'Нет в наличии'}, status.HTTP_204_NO_CONTENT)
        # берём из БД или создаём новую запись в корзине
        basket_object = OrderBasket.objects.get_or_create(
            items_id=item,
            user_tlg_id=user_tlg_id
        )
        # проверяем, что запись в БД не была создана
        if not basket_object[1]:
            # добавляем +1 к количеству товаров и сохраняем изменения в БД
            basket_object[0].items_number_in_basket += 1
            basket_object[0].save()
        result_object = OrderBasketSerializer(basket_object[0], many=False).data
        return Response(result_object, status.HTTP_201_CREATED)


# 5
class RemoveItemToBasket(APIView):
    '''Представление для удаления товара из корзины'''

    def get(self, request, format=None):
        # получение параметров запроса
        user_tlg_id = request.query_params.get('user_tlg_id')
        item_id = request.query_params.get('item_id')

        # берём объект товара
        item = Items.objects.get(pk=item_id)
        # добавляем +1 к общему числу товаров на "складе"
        item.number_of_items += 1
        item.save()

        # берём запись из корзины
        basket_object = OrderBasket.objects.get(
            items_id=item,
            user_tlg_id=user_tlg_id
        )
        # отнимаем от количества товаров 1
        basket_object.items_number_in_basket -= 1
        # если товаров меньше 1, то удаляем запись из БД корзины товаров
        if basket_object.items_number_in_basket < 1:
            basket_object.delete()
            result_object = {'deleted_from_basket': 'удалено из корзины'}
            return Response(result_object, status.HTTP_204_NO_CONTENT)
        else:
            # иначе сохраняем изменения
            basket_object.save()
            result_object = OrderBasketSerializer(basket_object, many=False).data
            return Response(result_object, status.HTTP_200_OK)


# 6
class OrdersView(APIView):
    '''Представление для добавления или обновления записей о заказах'''

    def get(self, request, format=None):
        '''Получение списка заказов для конкретного пользователя. Передать /?user_tlg_id=....'''

        user_tlg_id = request.query_params.get('user_tlg_id')
        if user_tlg_id:
            orders = Order.objects.filter(user_tlg_id=user_tlg_id)
            orders_serializer = OrderSerializer(orders, many=True).data
            return Response(orders_serializer, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        orders_pk = request.data.get('pk')
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            # хз почему, но когда использовал данные из сериализатора ничего не выходило
            order_object = Order.objects.update_or_create(pk=orders_pk, defaults={
                'user_tlg_id': request.data.get('user_tlg_id'),
                'pay_status': request.data.get('pay_status'),
                'execution_status': request.data.get('execution_status'),
                'order_items': request.data.get('order_items'),
                'result_orders_price': request.data.get('result_orders_price'),
            })

            result_object = OrderSerializer(order_object[0]).data
            return Response(result_object, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


# 7
class RemoveOrder(APIView):
    '''Представление для удаления заказа из БД. Передай /?pk заказа'''

    def get(self, request, format=None):
        order_pk = request.query_params.get('pk')
        if order_pk:
            Order.objects.get(pk=order_pk).delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


# 8
class ClearBasket(APIView):
    '''Представление для очистки корзины. Необходим параметр запроса /?user_tlg_id=...'''

    def get(self, request, format=None):
        # получение параметров запроса
        user_tlg_id = request.query_params.get('user_tlg_id')

        try:
            if user_tlg_id:
                # берём записи из корзины и удаляем их
                basket_object = OrderBasket.objects.filter(user_tlg_id=user_tlg_id).select_related('items_id')
            else:
                basket_object = OrderBasket.objects.all().select_related('items_id')
            for i_object in basket_object:
                pk = i_object.items_id.pk
                i_item = Items.objects.get(pk=pk)
                i_item.number_of_items += i_object.items_number_in_basket
                i_item.save()
                i_object.delete()
            answer_status = status.HTTP_200_OK
            result_object = {'basket_is_cleaned': 'корзина очищена'}

        except Exception:
            answer_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            result_object = {'some_exception': 'операция не выполнена из-за ошибки'}

        return Response(result_object, answer_status)


# 9
class ItemsDetailView(APIView):
    '''Представление для получения детальной информации о товаре'''

    def get(self, request, format=None):
        item_id = request.query_params.get('item_id')
        item_object = Items.objects.get(pk=item_id)
        result_object = ItemsSerializer(item_object, many=False).data
        return Response(result_object, status.HTTP_200_OK)