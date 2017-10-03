from django.contrib import admin

from .models import Tag, Article, Image


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'content_type', 'object_id')
    list_filter = ('content_type',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'created',
        'last_updated',
        'content',
        'description',
        'title',
        'slug',
        'status',
        'publish_date',
        'thumbnail',
    )
    list_filter = ('author', 'created', 'last_updated', 'publish_date')
    raw_id_fields = ('related_posts',)
    search_fields = ('slug',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'path')
