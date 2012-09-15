from strings.models import String
from django.contrib import admin
from django.conf import settings

class StringAdmin(admin.ModelAdmin):

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 device was"
        else:
            message_bit = "%s device were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    list_display = ['name', 'pub_date']
    ordering = ['-pub_date']
    actions = [make_published]

    fieldsets = [
        ('Content', {
            'fields': ['name', 'section', 'description', 'overlay_image', 'screen_width',
                'screen_height', 'screen_x', 'screen_y',]
        }),
    ]
    class Media:
        js = [
        ]

admin.site.register(String, StringAdmin)

