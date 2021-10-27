from django.contrib import admin
from news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("id", "title", "link", "creation_date", "upvotes", "author")
    search_fields = ("id", "author__startswith", "title__startswith")
    list_filter = ("creation_date",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("id", "author", "content", "creation_date", "news")
    search_fields = ("id", "author__startswith", "content__startswith", "news")
    list_filter = ("creation_date",)
