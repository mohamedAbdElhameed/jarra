from django.contrib import admin
from .models import MyUser, OrderSchema
# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'processor_id', 'order_id']
    search_fields = ['name', 'phone_number', 'email', 'order_id']
    list_filter = ['created', 'modified']

admin.site.register(MyUser, MyUserAdmin)

