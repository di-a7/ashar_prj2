from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id', 'name')
admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'price', 'category')
   search_fields = ('name',)
   list_filter = ('category',)
   
admin.site.register(Food, FoodAdmin)


admin.site.register(Table)


class OrderItemInline(admin.TabularInline):     # StackInline
   model = OrderItem
   autocomplete_fields = ('food',)
   extra = 0

class OrderAdmin(admin.ModelAdmin):
   list_display = ['id','user','quantity','total_price','status','payment_status']
   search_fields = ['user__username']
   list_filter = ['status','payment_status']
   inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)

# admin.site.register(OrderItem)

# table, order, orderitem admin customization
# add database settings to .env file