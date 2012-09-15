# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'String'
        db.create_table('strings_string', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('string_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('section', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('strings', ['String'])


    def backwards(self, orm):
        # Deleting model 'String'
        db.delete_table('strings_string')


    models = {
        'strings.string': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'String'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'string_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['strings']