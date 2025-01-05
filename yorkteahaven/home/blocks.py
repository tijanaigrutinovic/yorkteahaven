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
        label = "Navigacija"


class HeroBlock(StructBlock):
    title = CharBlock(required=True, help_text="Hero naslov")
    description = TextBlock(required=True, help_text="Opis hero sekcije")
    button_text = CharBlock(required=True, help_text="Tekst na dugmetu")
    button_link = URLBlock(required=True, help_text="Link za dugme")
    background_image = ImageChooserBlock(required=True, help_text="Pozadinska slika")

    class Meta:
        template = "blocks/hero.html"
        icon = "image"
        label = "Hero Sekcija"


class TeaInUKBlock(StructBlock):
    title = CharBlock(required=True, help_text="Naslov sekcije")
    description = TextBlock(required=True, help_text="Opis sekcije")
    image = ImageChooserBlock(required=True, help_text="Slika za sekciju")

    class Meta:
        template = "blocks/tea_in_uk.html"
        icon = "placeholder"
        label = "Tea in UK Sekcija"


class MostFamousTeasBlock(StructBlock):
    title = CharBlock(required=True, help_text="Naslov sekcije")
    teas = ListBlock(
        StructBlock(
            [
                ('name', CharBlock(required=True, help_text="Naziv čaja")),
                ('description', TextBlock(required=True, help_text="Opis čaja")),
                ('image', ImageChooserBlock(required=True, help_text="Slika čaja")),
            ]
        )
    )

    class Meta:
        template = "blocks/most_famous_teas.html"
        icon = "cup"
        label = "Najpoznatiji čajevi"


class HowToBrewBlock(StructBlock):
    title = CharBlock(required=True, help_text="Naslov sekcije")
    steps = ListBlock(
        CharBlock(required=True, help_text="Korak za pripremu čaja")
    )

    class Meta:
        template = "blocks/how_to_brew.html"
        icon = "list-ol"
        label = "Kako pripremiti čaj"


class FavoriteTeasBlock(StructBlock):
    title = CharBlock(required=True, help_text="Naslov sekcije")
    description = TextBlock(required=True, help_text="Poziv za korisnike da podele svoje omiljene čajeve")
    form_action = URLBlock(required=False, help_text="URL za slanje podataka formulara")

    class Meta:
        template = "blocks/favorite_teas.html"
        icon = "form"
        label = "Omiljeni čajevi"
