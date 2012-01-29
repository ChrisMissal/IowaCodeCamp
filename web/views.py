from django.core.context_processors import csrf
from django.forms.models import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
import datetime
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from web.models import Session, Event, Speaker, Sponsor

def home(request):
    return render_to_response('home.html')

def session_detail(request, id):
    session = Session.objects.get(id=id)
    return render_to_response('session.html', { 'session': session })

def session(request):
    event = Event.objects.latest()
    sessions = Session.objects.filter(event=event.id, confirmed=True)
    return render_to_response('sessions.html', { 'event': event, 'sessions': sessions })

def speaker_detail(request, id):
    speaker = Speaker.objects.get(id=id)
    return render_to_response('speaker.html', { 'speaker': speaker })

def speaker(request):
    event = Event.objects.latest()
    speakers = Speaker.objects.filter(event=event.id).filter(session__confirmed=True)
    # tie sessions and speakers together here
    return render_to_response('speakers.html', { 'event': event, 'speakers': speakers })

def sponsors(request):
    event = Event.objects.latest()
    sponsors = Sponsor.objects.filter(events=event.id)
    return render_to_response('sponsors.html', { 'event': event, 'sponsors': sponsors })

def about(request):
    #leaders = Leader.objects.get( - some criteria to load the leaders? - )
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')

def schedule(request):
    return render_to_response('schedule.html')

def new_submission(request):
    session_exclusions = ('event','speaker','room','start_time','end_time','slug','confirmed')
    SessionFormSet = modelformset_factory(Session, exclude=session_exclusions)
    SpeakerFormSet = modelformset_factory(Speaker, exclude=('slug',))
    if request.method == 'POST':
        session_formset = SessionFormSet(request.POST, prefix='session')
        speaker_formset = SpeakerFormSet(request.POST, request.FILES, prefix='speaker')
        if session_formset.is_valid() and speaker_formset.is_valid():
            # do something with the cleaned_data on the formsets.
            pass
    else:
        session_formset = SessionFormSet(Session.objects.none(), prefix='session')
        speaker_formset = SpeakerFormSet(Speaker.objects.none(), prefix='speaker')
    return render_to_response('submit.html', {
        'session_formset': session_formset,
        'speaker_formset': speaker_formset,
    })

def speaker_submit(request):
    SpeakerFormSet = modelformset_factory(Speaker, exclude=('slug',))
    if request.method == 'POST':
        formset = SpeakerFormSet(request.POST, request.FILES, Speaker.objects.none())
        if formset.is_valid():
            request.session['speaker'] = formset.model
            return HttpResponseRedirect('/session_submit')
        else:
            return HttpResponseRedirect('/speaker')
    else:
        c = RequestContext(request)
        c.update(csrf(request))
        speaker = Speaker.objects.none()
        speaker.event = Event.objects.latest()
        formset = SpeakerFormSet(queryset=speaker)

    return render_to_response('speaker_submit.html', {
        'formset': formset,
    }, c)

def submit(request):
    exclusions = ('event','speaker','room','start_time','end_time','slug','confirmed')
    SessionFormSet = modelformset_factory(Session, exclude=exclusions)
    if request.method == 'POST':
        formset = SessionFormSet(request.POST, request.FILES, Session.objects.none())
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/thanks')
        else:
            return HttpResponseRedirect('/submit')
    else:
        c = RequestContext(request)
        c.update(csrf(request))
        formset = SessionFormSet(queryset=Session.objects.none())

    return render_to_response('submit.html', {
        'formset': formset,
    }, c)

def thanks(request):
    return render_to_response('thanks.html')

# Extra pages below...

def error(request):
    return render_to_response('errors/404.html')

def throw(request):
    return render_to_response('errors/500.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)