from django.contrib.auth.decorators import login_required
from django.shortcuts import (
	redirect,
	render,
	render_to_response)

from courses.models import Course, Student, Teacher




def catalog(request):
	""" Shows the course catalog """
	ctx = {}
	ctx['courses'] = Course.objects.all()
	return render(request, 'courses/catalog.html', ctx)


@login_required
def teacher_portal(request):
	""" Shows the teacher portal, which has class info,
	    schedule deadlines..."""

	ctx = {}
	ctx['courses'] = Course.objects.filter(
		teacher=request.user.get_profile().teacher)
	return render(request, 'courses/portal/teacher.html', ctx)


def student_portal(request):
	""" Shows the student portal, which has class info,
	    schedule deadlines..."""
	return render(request, 'courses/portal/student.html', {})


@login_required
def personal_portal(request):
	""" Redirects to either student or teacher portal if logged in. """
	profile = request.user.get_profile()
	if hasattr(profile, 'student'):
		return student_portal(request)
	elif hasattr(profile, 'teacher'):
		return teacher_portal(request)

	return redirect('/')


def edit_course(request, id):
	""" Shows a view for editing a course. Only accessible by admins
		and teachers. """

	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		redirect('/')

	user = request.user
	if not (hasattr(user.get_profile(), 'teacher') or user.is_superuser):
		redirect('/')

	ctx = {}
	ctx['course'] = course
	return render(request, 'courses/edit_course.html', ctx)


def save_course(request, id):
	""" Save a course after editing. """

	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		redirect('/')

	user = request.user
	if not (hasattr(user.get_profile(), 'teacher') or user.is_superuser):
		redirect('/')

		
def course_portal(request, id):
	""" Shows a course homepage """
	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		redirect('show_catalog')

	ctx = {}
	ctx['course'] = course
	return render(request, 'courses/portal/course.html', ctx)
