# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Speaker.event'
        db.delete_column('web_speaker', 'event_id')

        # Changing field 'Speaker.image'
        db.alter_column('web_speaker', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Deleting field 'Sponsor.current'
        db.delete_column('web_sponsor', 'current')

        # Adding M2M table for field events on 'Sponsor'
        db.create_table('web_sponsor_events', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sponsor', models.ForeignKey(orm['web.sponsor'], null=False)),
            ('event', models.ForeignKey(orm['web.event'], null=False))
        ))
        db.create_unique('web_sponsor_events', ['sponsor_id', 'event_id'])

        # Changing field 'Sponsor.image'
        db.alter_column('web_sponsor', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

        # Adding field 'Session.event'
        db.add_column('web_session', 'event', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['web.Event']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Speaker.event'
        db.add_column('web_speaker', 'event', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['web.Event']), keep_default=False)

        # Changing field 'Speaker.image'
        db.alter_column('web_speaker', 'image', self.gf('django.db.models.fields.FilePathField')(max_length=100))

        # Adding field 'Sponsor.current'
        db.add_column('web_sponsor', 'current', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Removing M2M table for field events on 'Sponsor'
        db.delete_table('web_sponsor_events')

        # Changing field 'Sponsor.image'
        db.alter_column('web_sponsor', 'image', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Deleting field 'Session.event'
        db.delete_column('web_session', 'event_id')


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
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Speaker']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'web.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'web.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['web.Event']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['web']
