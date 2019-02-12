from django.contrib import admin

from activity import models


# Register your models here.
class DirectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug']}),
        ('Publication', {'fields': ['status']}),
        ('Content Details', {'fields': ['summary', 'content']}),
    ]

    prepopulated_fields = {'slug': ('title',)}

    search_fields = ['title']


admin.site.register(models.Direction, DirectionAdmin)
