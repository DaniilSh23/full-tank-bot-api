from django.contrib import admin
from bot_api.models import MediaForItems, Categories, Items, OrderBasket, Order, PaidOrder, OrderArchive


class CategoriesAdmin(admin.ModelAdmin):
    '''Регистрация модели категорий товаров в админ панели'''
    list_display = ['id', 'category_name']
    list_display_links = ['id', 'category_name']


class MediaForItemsAdminInlines(admin.StackedInline):
    '''Регистрация модели медиа файлов для выполненных работ в админ панели, в режиме инлайн'''
    model = MediaForItems


class ItemsAdmin(admin.ModelAdmin):
    '''Регистрация модели товаров в админ панели'''
    list_display = ['id', 'items_name', 'price', 'number_of_items', 'items_category']
    list_display_links = ['id', 'items_name', 'price', 'number_of_items', 'items_category']
    inlines = [MediaForItemsAdminInlines]


class OrderBasketAdmin(admin.ModelAdmin):
    '''Регистрация модели товаров из корзины в админ панели'''
    list_display = ['id', 'items_id', 'items_number_in_basket', 'user_tlg_id']
    list_display_links = ['id', 'items_id', 'items_number_in_basket', 'user_tlg_id']


class OrderArchiveAdmin(admin.ModelAdmin):
    '''Регистрация модели архива заказов в админ панели.'''
    list_display = ['id', 'order_id_before_receiving', 'datetime', 'result_orders_price']
    list_display_links = ['id', 'order_id_before_receiving', 'datetime', 'result_orders_price']


class OrderAdmin(admin.ModelAdmin):
    '''Регистрация модели заказа в админ панели'''
    list_display = ['id', 'user_tlg_id', 'datetime', 'pay_status', 'execution_status', 'order_items', 'result_orders_price']
    list_display_links = ['id', 'user_tlg_id', 'datetime', 'pay_status', 'execution_status', 'order_items', 'result_orders_price']


class PaidOrderAdmin(admin.ModelAdmin):
    '''Регистрация модели с информацией о поступившем платеже в админ панели'''
    list_display = ['id', 'order_id', 'total_price', 'datetime', 'customer_name']
    list_display_links = ['id', 'order_id', 'total_price', 'datetime', 'customer_name']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(OrderBasket, OrderBasketAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PaidOrder, PaidOrderAdmin)
admin.site.register(OrderArchive, OrderArchiveAdmin)