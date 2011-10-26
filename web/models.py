from django.db import models

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
        return "Iowa Code Camp %i" % self.id

class Attendee(models.Model):
    event = models.ForeignKey(Event)
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
    image = models.URLField()
    link = models.URLField()
    current = models.BooleanField() # or we just maintain a master list and turn them on/off

    class Admin:
        pass

class Speaker(models.Model):
    event = models.ForeignKey(Event)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    twitter = models.CharField(max_length=15) # twitter usernames cannot be over 15 characters
    link = models.URLField()
    image = models.FilePathField()

    class Admin:
        pass

class Session(models.Model):
    speaker = models.ForeignKey(Speaker)
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=2000)
    room = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Admin:
        pass