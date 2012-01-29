# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Speaker.email'
        db.add_column('web_speaker', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Speaker.email'
        db.delete_column('web_speaker', 'email')


    models = {
        'web.attendee': {
            'Meta': {'object_name': 'Attendee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Event']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'web.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Location']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'web.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'web.session': {
            'Meta': {'object_name': 'Session'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Speaker']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Event']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'db_index': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'web.sponsor': {
            'Meta': {'ordering': "['level']", 'object_name': 'Sponsor'},
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Event']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['web']
