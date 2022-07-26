from django.shortcuts import render
from .models import Members, Competition, Appointment, Events

# Create your views here.

# 首頁
def index(request):

    return render(request, "index/index.html")

# 成員
def members(request):

    members = Members.objects.all().order_by('id')

    context = {
        'members':members
    }

    return render(request, "members/members.html", context)

# 賽事
def competition(request):

    competition = Competition.objects.all().order_by('id')

    context = {
        'competition':competition
    }

    return render(request, "competition/competition.html", context)

# 預約友誼賽
def appointment(request):

    appointment = Appointment.objects.all().order_by('id')
    
    context = {
        'appointment':appointment
    }

    return render(request, "appointment/appointment.html", context)

# 活動公告
def events(request):
    
    events = Events.objects.all().order_by('id')
    
    context = {
        'events':events
    }

    return render(request, "events/events.html", context)