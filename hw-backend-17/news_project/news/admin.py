# Register your models here.
from django.contrib import admin

from .models import News, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5  # Show 5 empty comment slots


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    inlines = [CommentInline]


admin.site.register(Comment)
