# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'courses_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'courses', ['Student'])

        # Adding model 'Teacher'
        db.create_table(u'courses_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('min_grade', self.gf('django.db.models.fields.IntegerField')()),
            ('max_grade', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'courses', ['Teacher'])

        # Adding model 'Course'
        db.create_table(u'courses_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'courses', ['Course'])

        # Adding model 'CourseApplication'
        db.create_table(u'courses_courseapplication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applications', to=orm['courses.Course'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applcations', to=orm['courses.Student'])),
        ))
        db.send_create_signal(u'courses', ['CourseApplication'])

        # Adding model 'Timeslot'
        db.create_table(u'courses_timeslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.IntegerField')()),
            ('end_time', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'courses', ['Timeslot'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'courses_student')

        # Deleting model 'Teacher'
        db.delete_table(u'courses_teacher')

        # Deleting model 'Course'
        db.delete_table(u'courses_course')

        # Deleting model 'CourseApplication'
        db.delete_table(u'courses_courseapplication')

        # Deleting model 'Timeslot'
        db.delete_table(u'courses_timeslot')


    models = {
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'courses.courseapplication': {
            'Meta': {'object_name': 'CourseApplication'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['courses.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applcations'", 'to': u"orm['courses.Student']"})
        },
        u'courses.student': {
            'Meta': {'object_name': 'Student'},
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'courses.teacher': {
            'Meta': {'object_name': 'Teacher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'max_grade': ('django.db.models.fields.IntegerField', [], {}),
            'min_grade': ('django.db.models.fields.IntegerField', [], {})
        },
        u'courses.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'end_time': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['courses']