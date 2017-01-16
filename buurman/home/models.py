from django.db import models

from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from modelcluster.fields import ParentalKey

class HomePage(Page):
    pass


class Images(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        ImageChooserPanel('image')
    ]
    class Meta:
        abstract = True

class PhotoPageImages(Orderable, Images):
    page = ParentalKey('PhotoPage', related_name='related_images')


class PhotoPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('related_images', label="Foto"),
    ]
    pass
