from django.forms import ModelForm
from web.models import Session

class SessionForm(ModelForm):
    class Meta:
        model = Session
