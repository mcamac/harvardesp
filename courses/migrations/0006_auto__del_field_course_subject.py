# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Course.subject'
        db.delete_column(u'courses_course', 'subject_id')

        # Adding M2M table for field subjects on 'Course'
        m2m_table_name = db.shorten_name(u'courses_course_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'courses.course'], null=False)),
            ('subject', models.ForeignKey(orm[u'courses.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'subject_id'])


    def backwards(self, orm):
        # Adding field 'Course.subject'
        db.add_column(u'courses_course', 'subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='courses', to=orm['courses.Subject']),
                      keep_default=False)

        # Removing M2M table for field subjects on 'Course'
        db.delete_table(db.shorten_name(u'courses_course_subjects'))


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
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses'", 'symmetrical': 'False', 'to': u"orm['courses.Subject']"}),
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