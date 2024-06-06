from django.contrib import admin
from .models import Item

admin.site.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_datetime', 'title', 'content')