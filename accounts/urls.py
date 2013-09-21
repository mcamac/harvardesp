from django.conf.urls import patterns, include, url
from accounts.views import StudentCreateView, TeacherCreateView, StudentEditView, TeacherEditView

urlpatterns = patterns('accounts.views',
	url(r'^register/student$', StudentCreateView.as_view(),
		name='register_student'),
	url(r'^register/teacher$', TeacherCreateView.as_view(),
		name='register_teacher'),
	url(r'^edit/student/$', StudentEditView.as_view(),
		name='edit_student'),
	url(r'^edit/teacher/$', TeacherEditView.as_view(),
		name='edit_teacher'),
	url(r'^profile/$', 'profile', name='profile'),
)

urlpatterns += patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
		name='logout'),	
	url(r'^reset/pass/$', 'django.contrib.auth.views.password_reset',
		name='reset_password'),
	url(r'^reset/pass/done$', 'django.contrib.auth.views.password_reset_done',
		name='reset_password_done'),
	url(r'^reset/pass/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
		'django.contrib.auth.views.password_reset_confirm',
		{'post_reset_redirect': '/accounts/login' }),
    url(r'^reset/password/complete/$', 
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^change/pass/$', 'django.contrib.auth.views.password_change',
    	name='change_password'),
    url(r'^change/pass/done/$', 'django.contrib.auth.views.password_change_done'),

)