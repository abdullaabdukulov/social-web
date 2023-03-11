from django.contrib import admin
from .models import ShortCuts


@admin.register(ShortCuts)
class ShortCutsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created_at']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('title', )}
