from django.conf.urls import patterns, include, url

urlpatterns = patterns('courses.views',
	url(r'^catalog/$', 'catalog', name='catalog'),
	url(r'^me/$', 'personal_portal'),
	url(r'^(?P<id>\d+)$', 'course_portal'),
	url(r'^edit/(?P<id>\d+)$', 'edit_course', name='edit_course'),
)