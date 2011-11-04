from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import datetime
from web.models import Session, Event, Speaker

def home(request):
    return render_to_response('home.html')

def session_detail(request, id, tag):
    session = Session.objects.get(id=id)
    return render_to_response('session.html', { 'session': session })

def session(request):
    event = Event.objects.latest()
    sessions = Session.objects.filter(event=event.id)
    return render_to_response('sessions.html', { 'event': event, 'sessions': sessions })

def speaker_detail(request, id):
    speaker = Speaker.objects.get(id=id)
    return render_to_response('speaker.html', { 'speaker': speaker })

def speaker(request):
    event = Event.objects.latest()
    speakers = Speaker.objects.filter(event=event.id)
    # tie sessions and speakers together here
    return render_to_response('speakers.html', { 'event': event, 'speakers': speakers })

def about(request):
    #leaders = Leader.objects.get( - some criteria to load the leaders? - )
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')

def schedule(request):
    return render_to_response('schedule.html')

# Extra pages below...

def error(request):
    return render_to_response('errors/404.html')

def throw(request):
    return render_to_response('errors/500.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)