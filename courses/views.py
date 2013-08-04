from django.shortcuts import render_to_response

from courses.models import Course, Student, Teacher

def show_catalog(request):
	return render_to_response('courses/catalog.html', {})