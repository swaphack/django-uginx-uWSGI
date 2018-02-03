# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import Text, Resource, Language
from django.utils.html import format_html


class ResourceAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="/static{}" />'.format(obj.path))

    image_tag.short_description = 'Image'

    list_display = ['name', 'image_tag']

    readonly_fields = ('name', 'image_tag')


admin.site.register(Resource, ResourceAdmin)
admin.site.register(Text)
admin.site.register(Language)
