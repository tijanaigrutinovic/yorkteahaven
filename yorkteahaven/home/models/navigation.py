

class NavigationBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Unesite naslov linka")
    url = blocks.URLBlock(required=False, help_text="Unesite URL")
    page = blocks.PageChooserBlock(required=False, help_text="Izaberite stranicu")
    open_in_new_tab = blocks.BooleanBlock(required=False, help_text="Otvori u novom tabu")

    class Meta:
        template = "blocks/navigation.html"
        icon = "link"
        label = "Navigacija"