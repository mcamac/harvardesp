from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esp.views.home', name='home'),
    # url(r'^esp/', include('esp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^courses/', include('courses.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('core.urls')),
)
