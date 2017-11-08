from blog import models as bm
from rest_framework import viewsets, serializers, routers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = bm.Tag
        fields = ('tag')


class AuthorSerializer(serializers.BaseSerializer):
    name = serializers.CharField()


class BaseArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = bm.Article
        depth = 1


class ListArticleSerializer(BaseArticleSerializer):
    class Meta(BaseArticleSerializer.Meta):
        fields = ('author', 'publish_date', 'title', 'description', 'thumbnail', 'url', 'id')



class ArticleSerializer(BaseArticleSerializer):
    related_posts = ListArticleSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta(BaseArticleSerializer.Meta):
        fields = (
            'author', 'related_posts', 'publish_date',
            'last_updated', 'content', 'description',
            'title', 'tags', 'thumbnail', 'url', 'id'
        )


class ArticleAPI(viewsets.ModelViewSet):
    queryset = bm.Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = []

    def list(self, request):
        self.serializer_class = ListArticleSerializer
        return super().list(request)


class TagAPI(viewsets.ReadOnlyModelViewSet):
    queryset = bm.Tag.objects.all()
    serializer_class = TagSerializer


router = routers.DefaultRouter()
router.register(r'articles', ArticleAPI, base_name='article')
router.register(r'tags', TagAPI, base_name='tag')

urls = router.urls
