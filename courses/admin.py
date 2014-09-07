from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from flatblocks.models import FlatBlock

from courses.models import (
	Course,
	Student,
	Subject,
	Teacher,
	Timeslot,
	UserProfile)

admin_site = AdminSite()

class CourseAdmin(admin.ModelAdmin):
	pass

admin_site.register(Course, CourseAdmin)

admin_site.register(User)

class UserProfileAdmin(admin.ModelAdmin):
	pass

admin_site.register(UserProfile, UserProfileAdmin)


class StudentAdmin(admin.ModelAdmin):
	pass

admin_site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
	pass

admin_site.register(Teacher, TeacherAdmin)


class SubjectAdmin(admin.ModelAdmin):
	pass

admin_site.register(Subject, SubjectAdmin)


class TimeslotAdmin(admin.ModelAdmin):
	pass

admin_site.register(Timeslot, TimeslotAdmin)

class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')
    
    class Media:
	    js = [
	        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
	        '/static/tinymce_setup.js',
	    ]



admin_site.register(FlatBlock, FlatBlockAdmin)
