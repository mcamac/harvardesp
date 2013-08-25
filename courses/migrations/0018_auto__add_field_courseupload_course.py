# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CourseUpload.course'
        db.add_column(u'courses_courseupload', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='files', to=orm['courses.Course']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CourseUpload.course'
        db.delete_column(u'courses_courseupload', 'course_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'TBA'", 'max_length': '255'}),
            'max_enrollment': ('django.db.models.fields.IntegerField', [], {}),
            'max_grade': ('django.db.models.fields.IntegerField', [], {}),
            'min_grade': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prerequisites': ('django.db.models.fields.TextField', [], {}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses'", 'symmetrical': 'False', 'to': u"orm['courses.Subject']"}),
            'syllabus': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'courses'", 'to': u"orm['courses.Teacher']"}),
            'timeslots': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'courses'", 'symmetrical': 'False', 'to': u"orm['courses.Timeslot']"})
        },
        u'courses.courseapplication': {
            'Meta': {'object_name': 'CourseApplication'},
            'approved': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '15'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['courses.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['courses.Student']"})
        },
        u'courses.courseupload': {
            'Meta': {'object_name': 'CourseUpload'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['courses.Course']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'courses.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'emergency_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'emergency_city': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'emergency_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'emergency_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'emergency_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'emergency_primary_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'emergency_secondary_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'emergency_state': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'emergency_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'parent_first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent_primary_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parent_secondary_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courses.UserProfile']", 'unique': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'courses.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'courses.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'grad_year': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'primary_phone': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courses.UserProfile']", 'unique': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secondary_phone': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'courses.timeslot': {
            'Meta': {'object_name': 'Timeslot'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'courses.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['courses']