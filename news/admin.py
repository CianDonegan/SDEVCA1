from django.contrib import admin
from .models import NewsArticle, newsComment


class CommentInline(admin.TabularInline):
    model = newsComment
    extra = 0

class NewsArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
# Register your models here.
admin.site.register(NewsArticle,NewsArticleAdmin)
admin.site.register(newsComment)

# Register your models here.
