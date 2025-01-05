from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, StructBlock, CharBlock, PageChooserBlock, BooleanBlock, URLBlock, ListBlock
from wagtail.images.blocks import ImageBlock

class NavigationBlock(StructBlock):
    logo = ImageBlock(required=False)
    links = ListBlock(
        StructBlock(
            [
                ('title', CharBlock(required=True)),
                ('url', URLBlock(required=False)),
                ('page', PageChooserBlock(required=False)),
                ('open_in_new_tab', BooleanBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "blocks/navigation.html"  # Pazi na putanju
        icon = "link"
        label = "Navigacija"

class HomePage(Page):
    navigation = StreamField(
        [
            ("navigation", NavigationBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,  # Ovo je za Wagtail 4.0+
    )

    body = StreamField(
        [
            ("rich_text", RichTextBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,  # Ovo je za Wagtail 4.0+
    )

    content_panels = Page.content_panels + [
        FieldPanel("navigation"),
        FieldPanel("body"),
    ]
