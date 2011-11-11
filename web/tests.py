import unittest
from django.core.urlresolvers import reverse

from django.test import TestCase
from datetime import date
from icc.web.models import Event
from web.models import Session, Speaker
from web.services.converters import int2roman

class RomanNumeralTestCase(unittest.TestCase):
    def testInt(self):
        self.assertEquals('I', int2roman(1))
        self.assertEquals('IV', int2roman(4))
        self.assertEquals('V', int2roman(5))
        self.assertEquals('XV', int2roman(15))
        self.assertEquals('XIV', int2roman(14))

class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.first = Event.objects.create(id=1, location_id=0, date=date.today(), start_time='08:00', end_time='17:30')
        self.eighth = Event.objects.create(id=8, location_id=0, date=date.today(), start_time='08:00', end_time='17:30')

    def testString(self):
        self.assertEquals(self.first.__str__(), 'Iowa Code Camp I')
        self.assertEquals(self.eighth.__str__(), 'Iowa Code Camp VIII')

class SessionTestCase(unittest.TestCase):
    def setUp(self):
        self.one = Session.objects.create(event_id=1, title='Super Awesome Session Name', slug='super-awesome-session-name')
        self.two = Session.objects.create(event_id=2, title='Best Session Ever', slug='best-session-ever')

    def testUrls(self):
        self.assertEquals("/session/%s/super-awesome-session-name" % self.one.id, self.one.get_absolute_url())
        self.assertEquals("/session/%s/best-session-ever" % self.two.id, self.two.get_absolute_url())

    def testReverse(self):
        self.assertEquals("/session/%s/super-awesome-session-name" % self.one.id, reverse('session_detail',args=[self.one.id, self.one.slug]))

class SpeakerTestCase(unittest.TestCase):
    def setUp(self):
        self.one = Speaker.objects.create(slug='chris-missal')

    def testReverse(self):
        self.assertEquals("/speaker/%s/chris-missal" % self.one.id, reverse('speaker_detail', args=[self.one.id, self.one.slug]))