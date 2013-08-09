# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'courses_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'courses', ['UserProfile'])


        # Changing field 'Timeslot.start_time'
        db.alter_column(u'courses_timeslot', 'start_time', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Timeslot.end_time'
        db.alter_column(u'courses_timeslot', 'end_time', self.gf('django.db.models.fields.TimeField')())

    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'courses_userprofile')


        # Changing field 'Timeslot.start_time'
        db.alter_column(u'courses_timeslot', 'start_time', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Timeslot.end_time'
        db.alter_column(u'courses_timeslot', 'end_time', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_enrollment': ('django.db.models.fields.IntegerField', [], {}),
            'max_grade': ('django.db.models.fields.IntegerField', [], {}),
            'min_grade': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses'", 'to': u"orm['courses.Subject']"}),
            'timeslots': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses'", 'symmetrical': 'False', 'to': u"orm['courses.Timeslot']"})
        },
        u'courses.courseapplication': {
            'Meta': {'object_name': 'CourseApplication'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['courses.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['courses.Student']"})
        },
        u'courses.student': {
            'Meta': {'object_name': 'Student'},
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'courses.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'courses.teacher': {
            'Meta': {'object_name': 'Teacher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'courses.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'courses.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['courses']