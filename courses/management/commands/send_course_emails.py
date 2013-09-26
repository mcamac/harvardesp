from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from courses.models import Student, Course, CourseApplication, Timeslot


def mail_student(student):
    ctx = {}
    ctx['student'] = student

    timeslots = Timeslot.objects.all().order_by('start_time')
    applications = (CourseApplication.objects.filter(student=student)
                                     .exclude(approved='rejected'))
    print applications

    ctx['timeslots'] = timeslots
    ctx['courses'] = {}
    for t in timeslots:
        ctx['courses'][t.pk] = []
        
    for app in applications:
        ctx['courses'][app.course.timeslot.pk].append(app.course)

    ctx['courses_list'] = [(t, ctx['courses'][t.pk]) for t in timeslots]

    ctx['text_block'] = ''
    for t in timeslots:
        ctx['text_block'] += '%s:\n' % t
        for course in ctx['courses'][t.pk]:
            ctx['text_block'] += '%s - in room %s\n' % (course.name, course.location)

        ctx['text_block'] += '\n'

    email_text =  render_to_string('email/courses_list.txt', ctx)
    html_text =  render_to_string('email/courses_list.html', ctx)

    email = EmailMultiAlternatives('Your ESP Class Schedule', email_text, 
                         'harvardesp@gmail.com', [student.profile.user.email, 
                                                  student.parent_email],
                         ['camacho@college.harvard.edu'])
    email.attach_alternative(html_text, 'text/html')
    email.attach_file('courses/templates/email/documents/Map for ESP.gif')
    email.attach_file('courses/templates/email/documents/ESP Parking Information.doc')
    email.send()
    print 'Email sent to: %s, %s' % (student.profile.user.email, student.parent_email)


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):

        registered_students = filter(lambda s: s.applications.all().count() > 0,
                                     Student.objects.all())

        for student in registered_students:
            mail_student(student)

        print "%d emails sent." % len(registered_students)
