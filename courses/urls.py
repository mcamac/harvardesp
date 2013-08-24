from django.conf.urls import patterns, include, url

urlpatterns = patterns('courses.views',
	url(r'^catalog/$', 'catalog', name='catalog'),
	url(r'^me/$', 'personal_portal', name='personal_portal'),
	url(r'^(?P<id>\d+)$', 'course_portal', name='course_portal'),
	url(r'^edit/(?P<id>\d+)$', 'edit_course', name='edit_course'),
	url(r'^new/$', 'new_course', name='new_course'),
	url(r'^destroy/(?P<id>\d+)$', 'delete_course', name='delete_course'),
	url(r'^signaws/$', 'sign_s3', name='sign_s3'),
)