from django.db import models
from web.services.converters import int2roman

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Event(models.Model):
    location = models.ForeignKey(Location)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        get_latest_by = 'id'

    def __str__(self):
        return "Iowa Code Camp " + int2roman(self.id)
    
class Attendee(models.Model):
    event = models.ForeignKey(Event, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Sponsor(models.Model):
    PLATINUM = 10
    GOLD = 20
    SILVER = 30
    SUPPORTER = 40
    SPONSORSHIP_LEVELS = (
        (PLATINUM,  u'Platinum'),
        (GOLD,      u'Gold'),
        (SILVER,    u'Silver'),
        (SUPPORTER, u'Supporter')
    )
    level = models.IntegerField(choices=SPONSORSHIP_LEVELS)
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='sponsors/')
    link = models.URLField()
    events = models.ManyToManyField(Event, verbose_name="list of events")

    class Meta:
        ordering = ['level']
        
    def __str__(self):
        return self.name

class Speaker(models.Model):
    event = models.ForeignKey(Event)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=15) # twitter usernames cannot be over 15 characters
    link = models.URLField()
    image = models.FileField(upload_to='speakers/%Y/%m/%d/')
    slug = models.SlugField(max_length=100, null=True)

    @models.permalink
    def get_absolute_url(self):
        return 'icc.web.views.speaker_detail', [self.id, self.slug]

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
    slug = models.SlugField(max_length=100, null=True)
    confirmed = models.BooleanField(null=False, default=False)
    
    @models.permalink
    def get_absolute_url(self):
        return 'icc.web.views.session_detail', [self.id, self.slug]

    def __str__(self):
        return self.title + " by " + str(self.speaker)
