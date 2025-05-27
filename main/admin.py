from django.contrib import admin
from .models import Zapis
from .models import Post, Like

@admin.register(Zapis)
class ZapisAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'excurse', 'date', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date', 'created_at')
    ordering = ('-created_at',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "value", "created_at")