from django.contrib import admin
# from django.contrib.sessions.models import Session
from .models import MyUser


# class SessionAdmin(admin.ModelAdmin):
#     def _session_data(self, obj):
#         return obj.get_decoded()
#     list_display = ['session_key', '_session_data', 'expire_date']


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'processor_id', 'order_id']
    search_fields = ['name', 'phone_number', 'email', 'order_id']
    list_filter = ['created', 'modified']

admin.site.register(MyUser, MyUserAdmin)

# admin.site.register(Session, SessionAdmin)
