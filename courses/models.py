from django.db import models

class Student(models.Model):
	grade = models.IntegerField()


class Teacher(models.Model):
	"""ESP instructor"""
	institution = models.CharField(max_length=255)
	

class Subject(models.Model):
	"""ESP student"""
	name = models.CharField(max_length=255)


class Timeslot(models.Model):
	"""A time range in which courses may be held."""
	start_time = models.IntegerField()
	end_time = models.IntegerField()
	

class Course(models.Model):
	"""ESP course"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	prerequisites = models.TextField()

	min_grade = models.IntegerField()
	max_grade = models.IntegerField()

	max_enrollment = models.IntegerField()

	timeslots = models.ManyToManyField(Timeslot, related_name='courses')

	subject = models.ForeignKey(Subject, related_name='courses')


class CourseApplication(models.Model):
	course = models.ForeignKey(Course, related_name='applications')
	student = models.ForeignKey(Student, related_name='applications')




