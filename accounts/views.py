from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import (
	redirect,
	render,
	render_to_response)
from django.views.generic.edit import CreateView

from courses.models import StudentForm, TeacherForm


def do_login(request):
	if request.POST:
		pass
	else:
		pass
	return render(request, 'pages/home.html')

def do_logout(request):
	return render(request, 'pages/home.html')


def register_student(request):
	form = StudentForm()
	ctx = {'form': form}
	return render(request, 'accounts/register/student.html', ctx)

def register_teacher(request):
	pass

class StudentCreateView(CreateView):
	form_class = StudentForm
	template_name = "accounts/register/student.html"
	success_url = reverse_lazy("personal_portal")

class TeacherCreateView(CreateView):
	form_class = TeacherForm
	template_name = "accounts/register/teacher.html"
	success_url = reverse_lazy("personal_portal")
