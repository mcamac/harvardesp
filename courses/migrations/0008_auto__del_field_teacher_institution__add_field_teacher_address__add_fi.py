# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Teacher.institution'
        db.delete_column(u'courses_teacher', 'institution')

        # Adding field 'Teacher.address'
        db.add_column(u'courses_teacher', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Teacher.city'
        db.add_column(u'courses_teacher', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Teacher.state'
        db.add_column(u'courses_teacher', 'state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Teacher.zip_code'
        db.add_column(u'courses_teacher', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15),
                      keep_default=False)

        # Adding field 'Teacher.school'
        db.add_column(u'courses_teacher', 'school',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Teacher.major'
        db.add_column(u'courses_teacher', 'major',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Teacher.grad_year'
        db.add_column(u'courses_teacher', 'grad_year',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=7),
                      keep_default=False)

        # Adding field 'Student.address'
        db.add_column(u'courses_student', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Student.city'
        db.add_column(u'courses_student', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Student.state'
        db.add_column(u'courses_student', 'state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Student.zip_code'
        db.add_column(u'courses_student', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15),
                      keep_default=False)

        # Adding field 'Student.school'
        db.add_column(u'courses_student', 'school',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Student.parent_first_name'
        db.add_column(u'courses_student', 'parent_first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Student.parent_last_name'
        db.add_column(u'courses_student', 'parent_last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Student.parent_email'
        db.add_column(u'courses_student', 'parent_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)

        # Adding field 'Student.parent_primary_phone'
        db.add_column(u'courses_student', 'parent_primary_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Student.parent_secondary_phone'
        db.add_column(u'courses_student', 'parent_secondary_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Student.emergency_first_name'
        db.add_column(u'courses_student', 'emergency_first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Student.emergency_last_name'
        db.add_column(u'courses_student', 'emergency_last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Student.emergency_email'
        db.add_column(u'courses_student', 'emergency_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)

        # Adding field 'Student.emergency_primary_phone'
        db.add_column(u'courses_student', 'emergency_primary_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Student.emergency_secondary_phone'
        db.add_column(u'courses_student', 'emergency_secondary_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Student.emergency_address'
        db.add_column(u'courses_student', 'emergency_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Student.emergency_city'
        db.add_column(u'courses_student', 'emergency_city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Student.emergency_state'
        db.add_column(u'courses_student', 'emergency_state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'Student.emergency_zip_code'
        db.add_column(u'courses_student', 'emergency_zip_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Teacher.institution'
        db.add_column(u'courses_teacher', 'institution',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'Teacher.address'
        db.delete_column(u'courses_teacher', 'address')

        # Deleting field 'Teacher.city'
        db.delete_column(u'courses_teacher', 'city')

        # Deleting field 'Teacher.state'
        db.delete_column(u'courses_teacher', 'state')

        # Deleting field 'Teacher.zip_code'
        db.delete_column(u'courses_teacher', 'zip_code')

        # Deleting field 'Teacher.school'
        db.delete_column(u'courses_teacher', 'school')

        # Deleting field 'Teacher.major'
        db.delete_column(u'courses_teacher', 'major')

        # Deleting field 'Teacher.grad_year'
        db.delete_column(u'courses_teacher', 'grad_year')

        # Deleting field 'Student.address'
        db.delete_column(u'courses_student', 'address')

        # Deleting field 'Student.city'
        db.delete_column(u'courses_student', 'city')

        # Deleting field 'Student.state'
        db.delete_column(u'courses_student', 'state')

        # Deleting field 'Student.zip_code'
        db.delete_column(u'courses_student', 'zip_code')

        # Deleting field 'Student.school'
        db.delete_column(u'courses_student', 'school')

        # Deleting field 'Student.parent_first_name'
        db.delete_column(u'courses_student', 'parent_first_name')

        # Deleting field 'Student.parent_last_name'
        db.delete_column(u'courses_student', 'parent_last_name')

        # Deleting field 'Student.parent_email'
        db.delete_column(u'courses_student', 'parent_email')

        # Deleting field 'Student.parent_primary_phone'
        db.delete_column(u'courses_student', 'parent_primary_phone')

        # Deleting field 'Student.parent_secondary_phone'
        db.delete_column(u'courses_student', 'parent_secondary_phone')

        # Deleting field 'Student.emergency_first_name'
        db.delete_column(u'courses_student', 'emergency_first_name')

        # Deleting field 'Student.emergency_last_name'
        db.delete_column(u'courses_student', 'emergency_last_name')

        # Deleting field 'Student.emergency_email'
        db.delete_column(u'courses_student', 'emergency_email')

        # Deleting field 'Student.emergency_primary_phone'
        db.delete_column(u'courses_student', 'emergency_primary_phone')

        # Deleting field 'Student.emergency_secondary_phone'
        db.delete_column(u'courses_student', 'emergency_secondary_phone')

        # Deleting field 'Student.emergency_address'
        db.delete_column(u'courses_student', 'emergency_address')

        # Deleting field 'Student.emergency_city'
        db.delete_column(u'courses_student', 'emergency_city')

        # Deleting field 'Student.emergency_state'
        db.delete_column(u'courses_student', 'emergency_state')

        # Deleting field 'Student.emergency_zip_code'
        db.delete_column(u'courses_student', 'emergency_zip_code')


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
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courses.UserProfile']", 'unique': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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