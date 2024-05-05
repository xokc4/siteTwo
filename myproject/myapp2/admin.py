from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_number','registration_date']
    ordering=['registration_date']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Описание продукта (name)'


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','quantity','added_date']
    ordering = ['added_date','price','quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Описание продукта (name)'

class OrderAdmin(admin.ModelAdmin):
    list_display=['client_name','product_names','order_date']
    ordering = ['order_date']
    list_filter = ['order_date']

    def client_name(self, obj):
        return obj.client.name  # Предполагается, что у клиента есть поле 'name'
    client_name.short_description = 'Client Name'

    def product_names(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    product_names.short_description = 'Product Names'

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

# Register your models here.
