from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import datetime
from web.models import Session, Event

def home(request):
    return render_to_response('home.html')

def session(request):
    event = Event.objects.get(id=8)
    sessions = Session.objects.filter(event=8)
    return render_to_response('sessions.html', { 'event': event, 'sessions': sessions })

def error(request):
    return render_to_response('errors/404.html')

def throw(request):
    return render_to_response('errors/500.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)