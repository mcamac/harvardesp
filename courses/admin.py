from django.contrib import admin
from flatblocks.models import FlatBlock

from courses.models import (
	Course,
	Student,
	Subject,
	Teacher,
	Timeslot)

class CourseAdmin(admin.ModelAdmin):
	pass

admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
	pass

admin.site.register(Teacher, TeacherAdmin)


class SubjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subject, SubjectAdmin)


class TimeslotAdmin(admin.ModelAdmin):
	pass

admin.site.register(Timeslot, TimeslotAdmin)

class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')
    class Media:
	    js = [
	        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
	        '/static/tinymce_setup.js',
	    ] 

admin.site.register(FlatBlock, FlatBlockAdmin)
