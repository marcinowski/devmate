from django.contrib import admin

from .models import Tag, Article, Thumbnail


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
    )
    list_filter = ('author', 'created', 'last_updated', 'publish_date')
    raw_id_fields = ('related_posts',)
    search_fields = ('slug',)


@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ('id',)
