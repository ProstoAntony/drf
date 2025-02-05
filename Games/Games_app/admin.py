from django.contrib import admin
from . models import Game
from .models import Todo


admin.site.register(Game)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'created_at')
    list_filter = ('status', 'author')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

class TodoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description')
        }),
        ('Дополнительно', {
            'fields': ('status', 'author'),
            'classes': ('collapse',)
        }),
    )
list_filter = ('status', 'author')
search_fields = ('title', 'description')

actions = ['mark_as_completed']

def mark_as_completed(self, request, queryset):
    queryset.update(status='completed')
mark_as_completed.short_description = "Пометить как завершенные"
