from wagtail.blocks import (
    StructBlock, CharBlock, TextBlock, BooleanBlock, URLBlock,
    ListBlock, PageChooserBlock, RichTextBlock
)
from wagtail.images.blocks import ImageChooserBlock


class NavigationBlock(StructBlock):
    logo = ImageChooserBlock(required=False)
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
        template = "blocks/navigation.html"
        icon = "link"
        label = "Navigation"


class HeroBlock(StructBlock):
    image = ImageChooserBlock(required=True, help_text="Hero image")
    title = CharBlock(required=True, help_text="Hero title")
    description = TextBlock(required=False, help_text="Description")
    button_text = CharBlock(required=False, help_text="Button title")
    button_link = URLBlock(required=False, help_text="Button Link")

    class Meta:
        template = "blocks/hero.html"
        icon = "image"
        label = "Hero Section"


class TeaInUKBlock(StructBlock):
    title = CharBlock(required=True, help_text="Title")
    description = TextBlock(required=True, help_text="Description")
    fun_fact = CharBlock(required=False, help_text="Card Title")
    fun_fact_description = TextBlock(required=False, help_text="Card Description")
    class Meta:
        template = "blocks/tea_in_uk.html"
        icon = "placeholder"
        label = "Tea in UK"


class MostFamousTeasBlock(StructBlock):
    title = CharBlock(required=True, help_text="Naslov sekcije")
    teas = ListBlock(
        StructBlock(
            [
                ('image', ImageChooserBlock(required=True, help_text="Slika čaja")),
                ('name', CharBlock(required=True, help_text="Naziv čaja")),
                ('description', TextBlock(required=True, help_text="Opis čaja")),
            ]
        )
    )

    class Meta:
        template = "blocks/most_famous_teas.html"
        icon = "pick"
        label = "Famous Teas"


class HowToBrewBlock(StructBlock):
    title = CharBlock(required=True,)
    steps = ListBlock(
        StructBlock(
            [
                ('card_title', CharBlock(required=True, help_text="Card title")),
                ('card_description', TextBlock(required=True, help_text="Card Description")),
                ('tip_button', CharBlock(required=True, help_text="Button title")),
                ('tip_description', TextBlock(required=True, help_text="Tip Description")),

            ]
        )
    )

    class Meta:
        template = "blocks/how_to_brew.html"
        icon = "list-ol"
        label = "How to Brew"


class FavoriteTeasBlock(StructBlock):
    title = CharBlock(required=True, help_text="Title")
    description = TextBlock(required=True, help_text="Description")
    image = ImageChooserBlock(required=True, help_text="Hero image")
    

    class Meta:
        template = "blocks/favorite_teas.html"
        icon = "form"
        label = "Favorite Tea"
