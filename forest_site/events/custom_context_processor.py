from .models import Event


def latest_e(request):
    event_title = Event.objects.first()
    return {
       'first_event': event_title
    }
