from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import (
    redirect,
    render,
    render_to_response)
from django.views.generic.edit import CreateView, UpdateView

from courses.models import (
    StudentForm, TeacherForm, Student, Teacher,
    StudentEditForm, TeacherEditForm)


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

class StudentEditView(UpdateView):
    model = Student
    form_class = StudentEditForm
    template_name = "accounts/edit/student.html"
    success_url = reverse_lazy("edit_student")

    def get_object(self, queryset=None):
        return self.request.user.get_profile().student

class TeacherEditView(UpdateView):
    model = Teacher
    form_class = TeacherEditForm
    template_name = "accounts/edit/teacher.html"
    success_url = reverse_lazy("edit_teacher")

    def get_object(self, queryset=None):
        return self.request.user.get_profile().teacher

@login_required
def profile(request):
    """ Redirects to either student or teacher profile if logged in. """
    profile = request.user.get_profile()
    if hasattr(profile, 'student'):
        return redirect('edit_student')
    elif hasattr(profile, 'teacher'):
        return redirect('edit_teacher')

    return redirect('/')