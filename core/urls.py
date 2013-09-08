from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
	url(r'^$', 'show_home', name='show_home'),
	url(r'^about$', 'show_about', name='show_about'),
	url(r'^faq$', 'show_faq', name='show_faq'),
)