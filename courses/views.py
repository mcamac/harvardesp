import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import (
	get_object_or_404,
	redirect,
	render,
	render_to_response)
from django.template.loader import render_to_string

from django.http import HttpResponse, HttpResponseRedirect
from courses.models import (Course, Student, Teacher,
	CourseForm, CourseApplication,
	CourseUpload, CourseUploadForm)

from filetransfers.api import prepare_upload
import esp.settings as settings


def catalog(request):
	""" Shows the course catalog """
	ctx = {}
	ctx['courses'] = Course.objects.filter(approved=True)

	if not request.user.is_anonymous():
		profile = request.user.get_profile()
		if hasattr(profile, 'student'):
			applications = CourseApplication.objects.filter(
				student=profile.student)
			ctx['student'] = profile.student
			ctx['applications'] = {}
			for application in applications:
				ctx['applications'][application.course.name] = application

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
	student = request.user.get_profile().student
	ctx = {}
	applications = CourseApplication.objects.filter(
		student=student).select_related('course')
	ctx['applications'] = applications
	return render(request, 'courses/portal/student.html', ctx)


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
	view_url = reverse('edit_course', kwargs={'id':id})

	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		return redirect('/')

	user = request.user
	print hasattr(user.get_profile(), 'teacher') 
	if not (hasattr(user.get_profile(), 'teacher') or user.is_superuser):
		return redirect('/')

	if not (request.user.is_superuser or
			upload.course.teacher != request.user.get_profile().teacher):
		return HttpResponse(status=401)

	ctx = {}
	ctx['course'] = course
	if request.POST:
		ctx['form'] = CourseForm(request.POST, request.FILES, instance=course)
		print request.FILES
		if ctx['form'].is_valid():
			ctx['form'].save()
			return redirect(view_url)

	else:
		ctx['upload_url'], ctx['upload_data'] = prepare_upload(request, view_url)
		ctx['form'] = CourseForm(instance=course)
		print ctx
	return render(request, 'courses/edit_course.html', ctx)


@login_required
def new_course(request):
	""" Creates a new course and redirects to edit view """
	view_url = reverse('new_course')
	ctx = {}
	ctx['new_course'] = True
	ctx['upload_url'], ctx['upload_data'] = prepare_upload(request, view_url)
	if request.POST:
		ctx['form'] = CourseForm(request.POST)
		print ctx['form'].errors
		if ctx['form'].is_valid():
			course = ctx['form'].save(commit=False)
			course.teacher = request.user.get_profile().teacher
			course.save()
			ctx['form'].save_m2m()
			return redirect('personal_portal')
		return render(request, 'courses/edit_course.html', ctx)
	else:
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


@login_required
def manage_course(request, id):
	"""View for management, such as accepting students and uploading."""
	if not (request.user.is_superuser or
			upload.course.teacher != request.user.get_profile().teacher):
		return HttpResponse(status=401)

	ctx = {}
	course = get_object_or_404(Course, pk=id)
	ctx['course'] = course
	ctx['applications'] = CourseApplication.objects.filter(course=course).select_related('student')
	ctx['upload_form'] = CourseUploadForm()
	return render(request, "courses/manage.html", ctx)


@login_required
def apply_course(request, id):
	student = request.user.get_profile().student

	try:
		course = Course.objects.get(pk=id)
	except Course.DoesNotExist:
		return redirect('/')

	try:
		application = CourseApplication.objects.get(
			student=student, course=course)
	except CourseApplication.DoesNotExist:
		application = CourseApplication.objects.create(
			student=student, course=course, approved="pending")
		email = render_to_string("email/course_application.txt", {
			'course': course, 'student': student})
		html_email = render_to_string("email/course_application.html", {
			'course': course, 'student': student})
		send_mail('[Harvard ESP] Student Registration', email, 'harvardesp@gmail.com', (course.teacher.profile.user.email,))
	ctx = {}
	ctx['application'] = application
	ctx['course'] = course
	return render(request, "courses/apply_course.html", ctx)


@login_required
def unapply_course(request, id):
	student = request.user.get_profile().student
	course = get_object_or_404(Course, pk=id)

	try:
		application = CourseApplication.objects.get(
			student=student, course=course)
	except CourseApplication.DoesNotExist:
		return redirect('/')

	application.delete()

	ctx = {}
	ctx['course'] = course
	return render(request, "courses/unapply_course.html", ctx)


@login_required
def handle_application(request, application_id):
	teacher = request.user.get_profile().teacher
	action = request.GET.get('action', None)

	if not action:
		return None
	
	application = get_object_or_404(CourseApplication, pk=application_id)
	if action == 'accept':
		application.approved = "approved"
	elif action == 'reject':
		application.approved = "rejected"
	application.save()

	return HttpResponse("done")


@login_required
def course_upload(request, id):
	course = get_object_or_404(Course, pk=id)

	if request.POST:
		form = CourseUploadForm(request.POST, request.FILES)
		if form.is_valid():
			upload = CourseUpload.objects.create(
				course=course, name=form.cleaned_data['name'],
				upload=form.cleaned_data['upload'])
			upload.save()
			return redirect('manage_course', id=id)
		else:
			print form.errors

		pass
	else:
		pass

@login_required
def delete_upload(request, id):
	""" Deletes a course upload"""
	upload = get_object_or_404(CourseUpload, pk=id)
	if not (request.user.is_superuser or
			upload.course.teacher != request.user.get_profile().teacher):
		return HttpResponse(status=401)

	upload.delete()
	return redirect('manage_course', id=upload.course.pk)


@user_passes_test(lambda u: u.is_superuser)
def scheduler(request):
	courses = Course.objects.all()
	ctx = {}
	ctx['courses'] = json.dumps(list(courses.values('name', 'timeslots')))

	return render(request, "courses/scheduler.html", ctx)
