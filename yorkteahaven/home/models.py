from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from home.blocks import (
    NavigationBlock, HeroBlock, TeaInUKBlock,
    MostFamousTeasBlock, HowToBrewBlock, FavoriteTeasBlock
)
from wagtail.blocks import RichTextBlock


class HomePage(Page):
    navigation = StreamField(
        [
            ("navigation", NavigationBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,  
    )

    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("tea_in_uk", TeaInUKBlock()),
            ("most_famous_teas", MostFamousTeasBlock()),
            ("how_to_brew", HowToBrewBlock()),
            ("favorite_teas", FavoriteTeasBlock()),
            ("rich_text", RichTextBlock()),  
        ],
        null=True,
        blank=True,
        use_json_field=True, 
    )

    content_panels = Page.content_panels + [
        FieldPanel("navigation"),
        FieldPanel("body"),
    ]
 