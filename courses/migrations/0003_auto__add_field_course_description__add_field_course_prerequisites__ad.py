# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Course.description'
        db.add_column(u'courses_course', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Course.prerequisites'
        db.add_column(u'courses_course', 'prerequisites',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Course.min_grade'
        db.add_column(u'courses_course', 'min_grade',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)

        # Adding field 'Course.max_grade'
        db.add_column(u'courses_course', 'max_grade',
                      self.gf('django.db.models.fields.IntegerField')(default=12),
                      keep_default=False)

        # Adding field 'Course.max_enrollment'
        db.add_column(u'courses_course', 'max_enrollment',
                      self.gf('django.db.models.fields.IntegerField')(default=20),
                      keep_default=False)

        # Deleting field 'Teacher.max_grade'
        db.delete_column(u'courses_teacher', 'max_grade')

        # Deleting field 'Teacher.min_grade'
        db.delete_column(u'courses_teacher', 'min_grade')


    def backwards(self, orm):
        # Deleting field 'Course.description'
        db.delete_column(u'courses_course', 'description')

        # Deleting field 'Course.prerequisites'
        db.delete_column(u'courses_course', 'prerequisites')

        # Deleting field 'Course.min_grade'
        db.delete_column(u'courses_course', 'min_grade')

        # Deleting field 'Course.max_grade'
        db.delete_column(u'courses_course', 'max_grade')

        # Deleting field 'Course.max_enrollment'
        db.delete_column(u'courses_course', 'max_enrollment')

        # Adding field 'Teacher.max_grade'
        db.add_column(u'courses_teacher', 'max_grade',
                      self.gf('django.db.models.fields.IntegerField')(default=12),
                      keep_default=False)

        # Adding field 'Teacher.min_grade'
        db.add_column(u'courses_teacher', 'min_grade',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'courses.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'end_time': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['courses']