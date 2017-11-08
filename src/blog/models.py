from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.text import slugify, Truncator
from django.utils.translation import ugettext_lazy as _

from blog.managers import ArticleManager
from blog.services import get_random_thumbnail, THUMBNAILS_DIR


UserModel = get_user_model()


class Tag(models.Model):
    tag = models.SlugField(unique=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Article(models.Model):
    CONTENT_STATUS_DRAFT = 1
    CONTENT_STATUS_PUBLISHED = 2
    CONTENT_STATUS_CHOICES = (
        (CONTENT_STATUS_DRAFT, _("Draft")),
        (CONTENT_STATUS_PUBLISHED, _("Published")),
    )
    author = models.ForeignKey(UserModel, related_name='articles')
    related_posts = models.ManyToManyField("self", verbose_name="Related posts", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField(_("Content"), blank=True)  # todo: Custom content field + widget
    description = models.TextField(_("Description"), blank=True)
    title = models.CharField(_("Title"), max_length=500)  # fixme: ugettext
    slug = models.SlugField(_("Slug"), max_length=500, blank=True)  # fixme: ugettext
    tags = GenericRelation(Tag, related_query_name='articles')
    thumbnail = models.ImageField(upload_to=THUMBNAILS_DIR, default=get_random_thumbnail)
    status = models.IntegerField(
        _("Status"),
        choices=CONTENT_STATUS_CHOICES,
        default=CONTENT_STATUS_PUBLISHED,
        help_text=_(
            "With Draft chosen, will only be shown for admin users "
            "on the site."
        )
    )
    publish_date = models.DateTimeField(
        _("Published from"),
        help_text=_("With Published chosen, won't be shown until this time"),
        blank=True,
        null=True,
        db_index=True
    )

    objects = ArticleManager()

    def save(self, *args, **kwargs):
        """ Makes sure that:
          - the slug is generated
          - the publish date is set
        """
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        if not self.publish_date and self.status == self.CONTENT_STATUS_PUBLISHED:
            self.publish_date = datetime.now()
        if not self.description:
            self.description = Truncator(self.content).words(100, html=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})


class Image(models.Model):
    path = models.ImageField(upload_to='images/article_images/')


"""
https://sachinchoolur.github.io/angular-trix/
textangular.com
https://www.tinymce.com/  # not angular
https://github.com/summernote/angular-summernote
https://github.com/angular-ui/ui-tinymce
http://wanming.github.io/angular-editor/
"""
