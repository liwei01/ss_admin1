# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','pass_field','passwd','port','enable')

class NodeAdmin(admin.ModelAdmin):
    list_display = ('id','node_name','node_type','node_ip','node_method','node_info','node_status','node_order')

class PorductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','description', 'price', 'date_available')

class PrderAdmin(admin.ModelAdmin):
    list_display = ('id','order_number','order_user','order_product','create_time','activate')



admin.site.register(User,UserAdmin)
admin.site.register(Node,NodeAdmin)
admin.site.register(Product,PorductAdmin)
admin.site.register(Prder,PrderAdmin)