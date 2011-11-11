from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from web.views import current_datetime
from django.conf.urls.defaults import url, patterns

admin.autodiscover()

urlpatterns = patterns('icc.web.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^session/(?P<id>\d+)/(.*)', 'session_detail', {}, name='session_detail'),
    url(r'^sessions/$', 'session', name='sessions'),
    url(r'^speaker/(?P<id>\d+)/(.*)', 'speaker_detail', {}, name='speaker_detail'),
    url(r'^speakers/$', 'speaker', name='speakers'),
    url(r'^schedule/$', 'schedule', name='schedule'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^throw/$', 'throw'),
    url(r'^system-time/$', 'current_datetime', name='time'),
)

urlpatterns += patterns(
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'icc.web.views.error'