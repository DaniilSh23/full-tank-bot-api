from django.urls import path

from bot_api.views import CategoryView, ItemsListView, OrderBasketView, AddItemToBasket, RemoveItemToBasket, OrdersView, \
    RemoveOrder, ClearBasket, ItemsDetailView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('items/', ItemsListView.as_view(), name='items'),
    path('basket/', OrderBasketView.as_view(), name='basket'),
    path('add_items_in_basket/', AddItemToBasket.as_view(), name='add_items_in_basket'),
    path('remove_items_from_basket/', RemoveItemToBasket.as_view(), name='remove_items_from_basket'),
    path('orders/', OrdersView.as_view(), name='order'),
    path('remove_order/', RemoveOrder.as_view(), name='remove_order'),
    path('clear_basket/', ClearBasket.as_view(), name='clear_basker'),
    path('item_detail/', ItemsDetailView.as_view(), name='item_detail'),
]
