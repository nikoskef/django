from django.contrib import admin

from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'company')
    list_display_links = ('id', 'title')
    list_filter = ('company',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_per_page = 20

admin.site.register(Room, RoomAdmin)