from django.conf.urls import patterns, include, url

urlpatterns = patterns('courses.views',
	url(r'^catalog/$', 'show_catalog'),
)