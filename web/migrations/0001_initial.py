# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('web_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('web', ['Location'])

        # Adding model 'Event'
        db.create_table('web_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Location'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('web', ['Event'])

        # Adding model 'Attendee'
        db.create_table('web_attendee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Event'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('web', ['Attendee'])

        # Adding model 'Sponsor'
        db.create_table('web_sponsor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('web', ['Sponsor'])

        # Adding model 'Speaker'
        db.create_table('web_speaker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Event'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
        ))
        db.send_create_signal('web', ['Speaker'])

        # Adding model 'Session'
        db.create_table('web_session', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Speaker'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('web', ['Session'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('web_location')

        # Deleting model 'Event'
        db.delete_table('web_event')

        # Deleting model 'Attendee'
        db.delete_table('web_attendee')

        # Deleting model 'Sponsor'
        db.delete_table('web_sponsor')

        # Deleting model 'Speaker'
        db.delete_table('web_speaker')

        # Deleting model 'Session'
        db.delete_table('web_session')


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
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Speaker']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Event']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'web.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['web']
