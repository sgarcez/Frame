from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'core.views.home', name='home'),
        url(r'^work/$', 'core.views.home', name='work'),
        url(r'^work/(\d+)/$', 'core.views.home', name='project'),
        url(r'^work/(\d+)/case_study/$', 'core.views.home', name='case'),
        url(r'^contact/$', 'core.views.home', name='contact'),
)
