from django.contrib.auth.models import User
from django.db import models
from django import forms
from form_utils.forms import BetterForm, BetterModelForm

import esp.settings as settings

import datetime
import string
import random


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        user = self.user
        return u"%s %s" % (user.first_name, user.last_name)

class Student(models.Model):
    """ESP student"""
    profile = models.OneToOneField(UserProfile)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=63)
    state = models.CharField(max_length=63)
    zip_code = models.CharField(max_length=15)

    school = models.CharField(max_length=255)
    grade = models.IntegerField()

    phone = models.CharField(max_length=20)

    parent_first_name = models.CharField(max_length=50)
    parent_last_name = models.CharField(max_length=50)
    parent_email = models.EmailField()
    parent_primary_phone = models.CharField(max_length=20)
    parent_secondary_phone = models.CharField(max_length=20)

    emergency_first_name = models.CharField(max_length=50)
    emergency_last_name = models.CharField(max_length=50)
    emergency_email = models.EmailField()
    emergency_primary_phone = models.CharField(max_length=20)
    emergency_secondary_phone = models.CharField(max_length=20)
    emergency_address = models.CharField(max_length=255)
    emergency_city = models.CharField(max_length=63)
    emergency_state = models.CharField(max_length=63)
    emergency_zip_code = models.CharField(max_length=15)

    def __unicode__(self):
        user = self.profile.user
        return u"%s %s" % (user.first_name, user.last_name)

class StudentForm(BetterModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    def is_valid(self):
        return super(StudentForm, self).is_valid()

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError('An account already exists with that email address')
        return self.cleaned_data['email']

    def save(self, force_insert=False, force_update=False, commit=True):
        super(StudentForm, self).save(commit=False)
        data = self.cleaned_data
        user = User.objects.create(
            email=data['email'],
            username=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'])
        user.set_password(data['password'])
        user.save()
        user_profile = UserProfile.objects.create(user=user)
        # user_fields = ['email', 'password', 'first_name', 'last_name']
        # for field in user_fields:
        #   del self.cleaned_data[field]
        self.instance.profile = user_profile
        self.instance.save()
        return self.instance

    def clean(self):
        print "CLEANING.."
        return super(StudentForm, self).clean()



    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 
                  'address', 'city', 'state', 'zip_code',
                  'school', 'grade', 'parent_first_name',
                  'parent_last_name', 'parent_email', 'parent_primary_phone',
                  'parent_secondary_phone', 'emergency_primary_phone',
                  'emergency_first_name', 'emergency_last_name',
                  'emergency_secondary_phone', 'emergency_address',
                  'emergency_email',
                  'emergency_city', 'emergency_state', 'emergency_zip_code']


        fieldsets = [
            ('account', {
                'fields': ['email', 'password', 'first_name', 'last_name'],
                'legend': 'Account Details'
            }),
            ('personal', {
                'fields': ['address', 'city', 'state', 'zip_code'],
                'legend': 'Personal Details'
            }),
            ('education', {
                'fields': ['school', 'grade'],
                'legend': 'Education Details'
            }),
            ('parent', {
                'fields': ['parent_first_name', 'parent_last_name',
                           'parent_email', 'parent_primary_phone',
                           'parent_secondary_phone'],
                'legend': 'Parent/Guardian Details'
            }),
            ('emergency', {
                'fields': ['emergency_first_name', 'emergency_last_name',
                           'emergency_primary_phone',
                           'emergency_secondary_phone',
                           'emergency_email', 'emergency_address',
                           'emergency_city', 'emergency_state',
                           'emergency_zip_code'],
                'legend': 'Emergency Contact Details'
            })
        ]

        row_attrs = {
            'email': {'class': 'address'},
            'password': {'class': 'address'},
            'address': {'class': 'address break-after'},
            'zip_code': {'class': 'zip'},
            'school': {'class': 'address'},
            'parent_last_name': {'class': 'break-after'},
            'parent_email': {'class': 'address break-after'},
            'emergency_last_name': {'class': 'break-after'},
            'emergency_address': {'class':'address break-after'},
            'emergency_secondary_phone': {'class': 'break-after'},
            'emergency_zip_code': {'class': 'zip'}
        }

        for key in fields:
            if key not in row_attrs:
                row_attrs[key] = {'class': ''}
            row_attrs[key]['class'] += ' inline'

class Teacher(models.Model):
    """ESP instructor"""
    profile = models.OneToOneField(UserProfile)

    # Address info
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=63)
    state = models.CharField(max_length=63)
    zip_code = models.CharField(max_length=15)

    primary_phone = models.CharField(max_length=31)
    secondary_phone = models.CharField(max_length=31)

    # School info
    school = models.CharField(max_length=255)
    major = models.CharField(max_length=63)
    grad_year = models.CharField(max_length=7)

    def __unicode__(self):
        user = self.profile.user
        return u"%s %s" % (user.first_name, user.last_name)

class TeacherForm(BetterModelForm):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    def is_valid(self):
        return super(TeacherForm, self).is_valid()

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError('An account already exists with that email address')
        return self.cleaned_data['email']

    def save(self, force_insert=False, force_update=False, commit=True):
        super(TeacherForm, self).save(commit=False)
        print "VALIDATIng.."
        data = self.cleaned_data
        user = User.objects.create(
            email=data['email'],
            username=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'])
        user.set_password(data['password'])
        user.save()
        user_profile = UserProfile.objects.create(user=user)
        # user_fields = ['email', 'password', 'first_name', 'last_name']
        # for field in user_fields:
        #   del self.cleaned_data[field]
        self.instance.profile = user_profile
        self.instance.save()
        return self.instance

    def clean(self):
        return super(TeacherForm, self).clean()



    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 
                  'address', 'city', 'state', 'zip_code',
                  'primary_phone', 'secondary_phone',
                  'school', 'major', 'grad_year']


        fieldsets = [
            ('account', {
                'fields': ['first_name', 'last_name', 'email', 'password'],
                'legend': 'Account Details'
            }),
            ('personal', {
                'fields': ['address', 'city', 'state', 'zip_code',
                           'primary_phone', 'secondary_phone'],
                'legend': 'Personal Details'
            }),
            ('education', {
                'fields': ['school', 'major', 'grad_year'],
                'legend': 'Education Details'
            }),
        ]

        row_attrs = {
            'last_name': {'class': 'break-after'},
            'email': {'class': 'address'},
            'password': {'class': 'address'},
            'address': {'class': 'address break-after'},
            'zip_code': {'class': 'zip break-after'},
            'school': {'class': 'address'},
        }

        for key in fields:
            if key not in row_attrs:
                row_attrs[key] = {'class': ''}
            row_attrs[key]['class'] += ' inline'

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Timeslot(models.Model):
    """A time range in which courses may be held."""
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return "%s to %s" % (self.start_time.strftime("%I:%M %p").strip('0'),
                             self.end_time.strftime("%I:%M %p").strip('0'))


def content_file_name(instance, filename):
    now = datetime.datetime.now().date()
    return '/'.join([str(now.year), str(now.month), str(now.day),
                     str(instance.pk), filename])

class Course(models.Model):
    """ESP course"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    prerequisites = models.TextField()

    min_grade = models.IntegerField()
    max_grade = models.IntegerField()

    max_enrollment = models.IntegerField()

    syllabus = models.FileField(upload_to=content_file_name, null=True, blank=True)

    location = models.CharField(max_length=255, default="TBA")

    timeslots = models.ManyToManyField(Timeslot, related_name='courses')
    subjects = models.ManyToManyField(Subject, related_name='courses')

    teacher = models.ForeignKey(Teacher, related_name='courses')

    approved = models.BooleanField(default=False)

    timeslot = models.ForeignKey(Timeslot, related_name='confirmed_courses', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def grade_range(self):
        return "%d-%d" % (self.min_grade, self.max_grade)

class CourseForm(BetterModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    prerequisites = forms.CharField(widget=forms.Textarea)
    max_enrollment = forms.IntegerField()
    timeslots = forms.ModelMultipleChoiceField(queryset=Timeslot.objects.all())
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    syllabus = forms.FileField(required=False)


    class Meta:
        model = Course
        fields = ['name', 'description', 'prerequisites',
                  'min_grade', 'max_grade', 'max_enrollment',
                  'timeslots', 'subjects', 'syllabus']

        row_attrs = {
            'min_grade': {'class': 'inline'},
            'max_grade': {'class': 'inline'},
            'max_enrollment': {'class': 'inline break-after'},
            'timeslots': {'class': 'inline'},
            'subjects': {'class': 'inline'},
        }


class CourseApplication(models.Model):
    course = models.ForeignKey(Course, related_name='applications')
    student = models.ForeignKey(Student, related_name='applications')
    approved = models.CharField(default="pending", max_length=15)




def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def upload_file_name(instance, filename):
    now = datetime.datetime.now().date()
    return '/'.join([str(now.year), str(now.month), str(now.day),
                     id_generator() + '-' + filename])


class CourseUpload(models.Model):
    course = models.ForeignKey(Course, related_name='files')
    name = models.CharField(max_length=63)
    created_at = models.DateField(auto_now_add=True)
    upload = models.FileField(upload_to=upload_file_name)


class CourseUploadForm(BetterModelForm):
    name = models.CharField(max_length=100)
    upload = models.FileField(upload_to=upload_file_name)

    from django.template.defaultfilters import filesizeformat

    def clean_upload(self):
        content = self.cleaned_data['upload']
        content_type = content.content_type
        if content_type in settings.CONTENT_TYPES:
            if content._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size))
        else:
            raise forms.ValidationError('File type %s is not supported' % content_type)
        return content

    class Meta:
        model = CourseUpload
        fields = ['name', 'upload']

        row_attrs = {
            'name': {'classes': 'inline'}
        }