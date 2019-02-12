from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin
from pages import models


# Register your models here.
class PageAdmin(TabbedTranslationAdmin):

    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
        ('Publication', {'fields': ['status']}),
        ('Content Details', {'fields': ['summary', 'content', 'head_image']}),
    ]

    prepopulated_fields = {'slug': ('title',)}

    search_fields = ['title']


admin.site.register(models.Page, PageAdmin)
