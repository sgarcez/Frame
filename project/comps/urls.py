from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'comps.views.test', name='comps_test'),
)
