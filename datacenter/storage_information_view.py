from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    for visiter in Visit.objects.filter(leaved_at__isnull=True):
        non_closed_visits.append({
            'who_entered': visiter.passcard,
            'entered_at': visiter.entered_at,
            'duration': get_duration(visiter.entered_at),
            'is_strange': is_visit_long(get_duration(visiter.entered_at,visiter.leaved_at))
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
