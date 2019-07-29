from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Category,Comment,News
class CommentInline(admin.StackedInline):
    model=Comment
class RegNews(admin.ModelAdmin,AdminSite):
    site_title='News Finder'
    index_title='articles'
    
    inlines=[CommentInline,]
    list_display=['headline','author',]
admin.site.register(Category)
admin.site.register(News,RegNews)