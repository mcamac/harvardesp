# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'courses_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'courses', ['Subject'])

        # Adding field 'Course.subject'
        db.add_column(u'courses_course', 'subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', related_name='courses', to=orm['courses.Subject']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'courses_subject')

        # Deleting field 'Course.subject'
        db.delete_column(u'courses_course', 'subject_id')


    models = {
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses'", 'to': u"orm['courses.Subject']"})
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