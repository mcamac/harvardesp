from django.contrib.auth.decorators import login_required
from django.shortcuts import (
	redirect,
	render,
	render_to_response)

from django.http import HttpResponseRedirect
from courses.models import Course, Student, Teacher, CourseForm

import esp.settings as settings


def catalog(request):
	""" Shows the course catalog """
	ctx = {}
	ctx['courses'] = Course.objects.filter(approved=True)
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


@login_required
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
	if request.POST:
		ctx['form'] = CourseForm(request.POST, instance=course)
		print ctx['form'].full_clean()
		if ctx['form'].is_valid():
			ctx['form'].save()

	else:
		ctx['form'] = CourseForm(instance=course)
	return render(request, 'courses/edit_course.html', ctx)


@login_required
def new_course(request):
	""" Creates a new course and redirects to edit view """
	ctx = {}
	if request.POST:
		ctx['form'] = CourseForm(request.POST)
		if ctx['form'].is_valid():
			course = ctx['form'].save(commit=False)
			course.teacher = request.user.get_profile().teacher
			course.save()
			ctx['form'].save_m2m()
			return redirect('personal_portal')
		return render(request, 'course/edit_course.html', ctx)
	else:
		ctx = {}
		ctx['new_course'] = True
		ctx['form'] = CourseForm()
		return render(request, 'courses/edit_course.html', ctx)


def delete_course(request, id):
	""" Deletes a course """
	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		redirect('/')

	course.delete()
	return redirect('personal_portal')


def course_portal(request, id):
	""" Shows a course homepage """
	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		redirect('show_catalog')

	ctx = {}
	ctx['course'] = course
	return render(request, 'courses/portal/course.html', ctx)


def sign_s3(request):
	AWS_ACCESS_KEY = settings.AWS_ACCESS_KEY_ID
	AWS_SECRET_KEY = settings.AWS_SECRET_ACCESS_KEY
	S3_BUCKET = settings.S3_BUCKET

	object_name = request.args.get('s3_object_name')
	mime_type = request.args.get('s3_object_type')

	expires = int(time.time()+10)
	amz_headers = "x-amz-acl:public-read"

	put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

	signature = base64.encodestring(hmac.new(AWS_SECRET_KEY,put_request, sha).digest())
	signature = urllib.quote_plus(signature.strip())

	url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

	return json.dumps({
	    'signed_request': '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
	     'url': url
	  })
