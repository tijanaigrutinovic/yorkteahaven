from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel
from wagtailseo.models import SeoMixin

from wagtail.blocks.NavigationBlock


from core.models.base import BaseHomePage


class HomePage(BaseHomePage):
    body = StreamField([
        ('navigation', NavigationBlock()),
             
    ],
    null = True,
    blank = True,
    use_json_field = True,                  
    )
    
   
HomePage.content_panels = [
    FieldPanel('title', classname="full title", help_text = 'Page Title'),
    FieldPanel('body'),
]
HomePage.promote_panels = SeoMixin.seo_panels


