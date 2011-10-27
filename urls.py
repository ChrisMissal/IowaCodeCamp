from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from web.views import current_datetime

admin.autodiscover()

urlpatterns = patterns('icc.web.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^session/(\d+)/$', 'session_detail'),
    url(r'^sessions/', 'session'),
    url(r'^throw/', 'throw'),
    url(r'^system-time/', 'current_datetime', name='time'),
)

urlpatterns += patterns(
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'icc.web.views.error'