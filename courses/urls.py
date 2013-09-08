from django.conf.urls import patterns, url

urlpatterns = patterns('courses.views',
	url(r'^catalog/$', 'catalog', name='catalog'),
	url(r'^me/$', 'personal_portal', name='personal_portal'),
	url(r'^(?P<id>\d+)$', 'course_portal', name='course_portal'),
	url(r'^edit/(?P<id>\d+)$', 'edit_course', name='edit_course'),
	url(r'^manage/(?P<id>\d+)$', 'manage_course', name='manage_course'),
	url(r'^apply/(?P<id>\d+)$', 'apply_course', name='apply_course'),
	url(r'^unapply/(?P<id>\d+)$', 'unapply_course', name='unapply_course'),
	url(r'^doupload/(?P<id>\d+)$', 'course_upload', name='course_upload'),
	url(r'^new/$', 'new_course', name='new_course'),
	url(r'^scheduler/$', 'scheduler', name='scheduler'),
	url(r'^destroy/(?P<id>\d+)$', 'delete_course', name='delete_course'),
	url(r'^application/(?P<application_id>\d+)$', 'handle_application',
		name='handle_application'),
	url(r'^uploads/delete/(?P<id>\d+)$', 'delete_upload', name='delete_upload')
)