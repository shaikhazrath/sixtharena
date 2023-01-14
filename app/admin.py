from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
	list_display = ['id','user','name']
	

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['id','title','selling_price']
 

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ['message']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
	list_display = ['id','user','product']



@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
	list_display = ['id','user','status']