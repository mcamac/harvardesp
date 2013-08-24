from django.conf.urls import patterns, include, url
from accounts.views import StudentCreateView, TeacherCreateView

urlpatterns = patterns('accounts.views',
	url(r'^register/student$', StudentCreateView.as_view(),
		name='register_student'),
	url(r'^register/teacher$', TeacherCreateView.as_view(),
		name='register_teacher'),
)

urlpatterns += patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
		name='logout'),	
)