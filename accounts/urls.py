from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
	url(r'^register/student$', 'register_student', name='register_student'),
	url(r'^register/teacher$', 'register_teacher', name='register_teacher'),
)

urlpatterns += patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
		name='logout'),	
)