from django.db import models
from web.services.converters import int2roman, tagify

class Location(models.Model):
    name = models.CharField(max_length=30)

    class Admin:
        pass

    def __str__(self):
        return self.name

class Event(models.Model):
    location = models.ForeignKey(Location)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Admin:
        pass

    def __str__(self):
        return "Iowa Code Camp " + int2roman(self.id)

class Attendee(models.Model):
    event = models.ForeignKey(Event, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    class Admin:
        pass

class Sponsor(models.Model):
    #event = models.ForeignKey(Event) # not sure if this is a good route to go
    SPONSORSHIP_LEVELS = (
        (u'PL', u'Platinum'),
        (u'GO', u'Gold'),
        (u'SI', u'Silver'),
        (u'SP', u'Supporter')
    )
    level = models.CharField(max_length=2, choices=SPONSORSHIP_LEVELS)
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='sponsors/')
    link = models.URLField()
    events = models.ManyToManyField(Event, verbose_name="list of events")

    class Admin:
        pass

class Speaker(models.Model):
    event = models.ForeignKey(Event)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=15) # twitter usernames cannot be over 15 characters
    link = models.URLField()
    image = models.FileField(upload_to='speakers/%Y/%m/%d/')

    class Admin:
        pass

    def get_absolute_url(self):
        return "/speaker/%i/" % self.id

    def __str__(self):
        return self.first_name + " " + self.last_name

class Session(models.Model):
    event = models.ForeignKey(Event, null=False)
    speaker = models.ForeignKey(Speaker)
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=2000)
    room = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def get_absolute_url(self):
        return ("/session/%i/" % self.id) + tagify(self.title)
    
    class Admin:
        pass