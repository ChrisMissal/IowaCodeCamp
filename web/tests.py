import unittest

from django.test import TestCase
from datetime import date
from icc.web.models import Event
from web.models import Session
from web.services.converters import int2roman, tagify

class RomanNumeralTestCase(unittest.TestCase):
    def testInt(self):
        self.assertEquals('I', int2roman(1))
        self.assertEquals('IV', int2roman(4))
        self.assertEquals('V', int2roman(5))
        self.assertEquals('XV', int2roman(15))
        self.assertEquals('XIV', int2roman(14))

class TokenizeTestCase(unittest.TestCase):
    def test(self):
        self.assertEquals('super-neato', tagify('Super Neato'))
        self.assertEquals('something-normal', tagify('Something, Normal!'))
        self.assertEquals('using-mvvm-frameworks', tagify('Using MVVM Frameworks'))
        self.assertEquals('the-tasty-flavors-of-entity-framework-41', tagify('The Tasty Flavors of Entity Framework 4.1'))
        self.assertEquals('programming-with-the-dot-net-async-ctp', tagify('Programming with the .NET Async CTP'))
        self.assertEquals('oauth-open-authentication-for-your-api', tagify('OAuth - Open Authentication for your API'))
        self.assertEquals('becoming-a-data-savant-correct-data-in-a-crunch', tagify('Becoming a Data Savant: Correct Data in a Crunch!'))
        self.assertEquals('is-f-sharp-the-new-perl', tagify('Is F# the new Perl?'))
        self.assertEquals('amateur-pro-or-somewhere-in-between', tagify('Amateur, Pro, or somewhere in between?'))
        self.assertEquals('my-love-hate-relationship-with-mobile-development', tagify('My love/hate relationship with mobile development'))
        self.assertEquals('f-sharp-c-sharp-what-f-sharp-does-that-you-cant-easily-do-in-c-sharp', tagify('F# > C# - What F# does that you can''t (easily) do in C#'))
        self.assertEquals('twenty-ways-to-make-your-site-faster-and-easier-to-work-with-on-the-cheap', tagify('Twenty Ways to Make Your Site Faster (and Easier to Work With) on the Cheap!'))
        self.assertEquals('how-ruby-is-making-me-a-better-c-sharp-developer', tagify('How Ruby Is Making Me a Better C# Developer'))
        self.assertEquals('startup-q-and-a', tagify('Startup Q&A'))
        self.assertEquals('startup-q-and-a', tagify('Startup Q & A'))
        self.assertEquals('getting-funcy-with-c-sharp-and-f-sharp', tagify('Getting Func-y with C# and F#'))
        self.assertEquals('dot-net-performance-diagnostics-where-to-start', tagify('.NET Performance Diagnostics - Where to Start'))

class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.first = Event.objects.create(id=1, location_id=0, date=date.today(), start_time='08:00', end_time='17:30')
        self.eighth = Event.objects.create(id=8, location_id=0, date=date.today(), start_time='08:00', end_time='17:30')

    def testString(self):
        self.assertEquals(self.first.__str__(), 'Iowa Code Camp I')
        self.assertEquals(self.eighth.__str__(), 'Iowa Code Camp VIII')

class SessionTestCase(unittest.TestCase):
    def setUp(self):
        self.one = Session.objects.create(id=45, event_id=1, title='Super Awesome Session Name')
        self.two = Session.objects.create(id=99, event_id=1, title='Best Session Ever')

    #def testTagifyTitle(self):
    #    self.assertEquals("best-session-ever", tagify(self.two.title))

    def testUrls(self):
        self.assertEquals("/session/45/super-awesome-session-name", self.one.get_absolute_url())
        self.assertEquals("/session/99/best-session-ever", self.two.get_absolute_url())