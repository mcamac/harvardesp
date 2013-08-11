from django.contrib.auth.models import User
from django.db import models
from django import forms


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

class StudentForm(forms.ModelForm):
	email = forms.EmailField(label="Email")
	password = forms.CharField(widget=forms.PasswordInput)
	parent_email = forms.EmailField()

	class Meta:
		model = Student
		fields = ['address', 'city', 'state', 'zip_code',
				  'school', 'grade', 'parent_first_name',
				  'parent_last_name', 'parent_email', 'parent_primary_phone',
				  'parent_secondary_phone', 'emergency_primary_phone',
				  'emergency_secondary_phone', 'emergency_address',
				  'emergency_city', 'emergency_state', 'emergency_zip_code']




class Teacher(models.Model):
	"""ESP instructor"""
	profile = models.OneToOneField(UserProfile)

	# Address info
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=63)
	state = models.CharField(max_length=63)
	zip_code = models.CharField(max_length=15)

	# School info
	school = models.CharField(max_length=255)
	major = models.CharField(max_length=63)
	grad_year = models.CharField(max_length=7)

	def __unicode__(self):
		user = self.profile.user
		return u"%s %s" % (user.first_name, user.last_name)

class Subject(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name


class Timeslot(models.Model):
	"""A time range in which courses may be held."""
	start_time = models.TimeField()
	end_time = models.TimeField()

	def __unicode__(self):
		return "%s to %s" % (self.start_time.strftime("%I:%M %p"),
							 self.end_time.strftime("%I:%M %p"))


class Course(models.Model):
	"""ESP course"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	prerequisites = models.TextField()

	min_grade = models.IntegerField()
	max_grade = models.IntegerField()

	max_enrollment = models.IntegerField()

	location = models.CharField(max_length=255)

	timeslots = models.ManyToManyField(Timeslot, related_name='courses')
	subjects = models.ManyToManyField(Subject, related_name='courses')

	teacher = models.ForeignKey(Teacher, related_name='courses')

	def __unicode__(self):
		return self.name

class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea)
	prerequisites = forms.CharField(widget=forms.Textarea)
	max_enrollment = forms.IntegerField()
	timeslots = forms.ModelMultipleChoiceField(queryset=Timeslot.objects.all())
	subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())

	class Meta:
		model = Course
		fields = ['name', 'description', 'prerequisites',
			      'min_grade', 'max_grade', 'max_enrollment',
			      'timeslots', 'subjects']


class CourseApplication(models.Model):
	course = models.ForeignKey(Course, related_name='applications')
	student = models.ForeignKey(Student, related_name='applications')




