from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, is_visit_long
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404


def passcard_info_view(request, passcode):
    this_passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for this_passcard_visit in get_list_or_404(Visit, passcard=this_passcard):
        this_passcard_visits.append({
            'entered_at': this_passcard_visit.entered_at,
            'duration': get_duration(this_passcard_visit.entered_at),
            'is_strange': is_visit_long(get_duration(this_passcard_visit.entered_at,this_passcard_visit.leaved_at))
        })

    context = {
        'passcard': this_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
