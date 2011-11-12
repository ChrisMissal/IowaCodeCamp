from web.models import Location, Event, Attendee, Sponsor, Speaker, Session
from django.contrib import admin

#class SessionAdmin(admin.ModelAdmin):
#    fields = ("speaker", "event", "title", "desc", "slug")
#    prepopulated_fields = {"slug":("title",) }

admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Sponsor)
admin.site.register(Speaker)
admin.site.register(Session)
