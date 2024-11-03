from django.contrib import admin
from .models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ( 'id','name','age', 'gender', 'occupation', 'created')  # Hiển thị các trường `id` và `name` trong danh sách

admin.site.register(Info, InfoAdmin)