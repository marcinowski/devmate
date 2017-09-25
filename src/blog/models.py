from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

CONTENT_STATUS_DRAFT = 1
CONTENT_STATUS_PUBLISHED = 2
CONTENT_STATUS_CHOICES = (
    (CONTENT_STATUS_DRAFT, _("Draft")),
    (CONTENT_STATUS_PUBLISHED, _("Published")),
)

UserModel = get_user_model()


class Tag(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Article(models.Model):
    author = models.ForeignKey(UserModel, related_name='articles')
    related_posts = models.ManyToManyField("self", verbose_name="Related posts", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField(_("Content"), blank=True)  # todo: Custom content field + widget
    description = models.TextField(_("Description"), blank=True)
    title = models.CharField(_("Title"), max_length=500)  # fixme: ugettext
    slug = models.SlugField(_("Slug"), max_length=500, blank=True)  # fixme: ugettext
    tags = GenericRelation(Tag, related_query_name='articles')
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


class Thumbnail(models.Model):
    pass


"""
https://sachinchoolur.github.io/angular-trix/
textangular.com
https://www.tinymce.com/  # not angular
https://github.com/summernote/angular-summernote
https://github.com/angular-ui/ui-tinymce
http://wanming.github.io/angular-editor/
"""
