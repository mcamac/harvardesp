from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
)

urlpatterns += patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
		name='logout'),
)