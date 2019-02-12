from modeltranslation.translator import register, TranslationOptions
from pages.models import Page


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'content')
