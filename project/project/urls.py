from django.conf.urls import patterns, include, url
from django.contrib import admin
# from api import v1_api
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include('comps.urls')),
        # url(r'api/', include(v1_api.urls)),
        url(r'^grappelli', include('grappelli.urls')),
        )

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
   )
   
