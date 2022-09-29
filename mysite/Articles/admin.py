from django.contrib import admin
from . import models

class CommentInline(admin.TabularInline):
    model = models.Commet

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Commet)