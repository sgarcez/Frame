from strings.models import String
from django.contrib import admin
from django.conf import settings


class StringAdmin(admin.ModelAdmin):

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 feature was"
        else:
            message_bit = "%s feature were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    list_display = ['string_id', 'content', 'pub_date']
    ordering = ['-pub_date']
    actions = [make_published]

    fieldsets = [
        ('Content', {
            'fields': ['string_id', 'description', 'content', 'section', ]
        }),
    ]

    class Media:
        js = [
              settings.STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              settings.STATIC_URL + 'tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(String, StringAdmin)
