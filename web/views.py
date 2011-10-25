from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def home(request):
    speakers = [ { 'name': 'Chris Missal', 'session': 'jQuery Plugin Templates' }, { 'name': 'Zac Harlan', 'session': 'Data Correctness' } ]
    return render_to_response('home.html', { 'speakers': speakers })

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)