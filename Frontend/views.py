from django.shortcuts import render

# Create your views here.

# 首頁
def index(request):
    # news = News.objects.all().order_by('id')
    # context = {
    #     'news':news
    # }
    return render(request, "index/index.html")

# 成員
def members(request):
    # news = News.objects.all().order_by('id')
    # context = {
    #     'news':news
    # }
    return render(request, "members/members.html")

# 賽事
def competition(request):
    # news = News.objects.all().order_by('id')
    # context = {
    #     'news':news
    # }
    return render(request, "competition/competition.html")

# 預約友誼賽
def appointment(request):
    # news = News.objects.all().order_by('id')
    # context = {
    #     'news':news
    # }
    return render(request, "appointment/appointment.html")

# 活動公告
def events(request):
    # news = News.objects.all().order_by('id')
    # context = {
    #     'news':news
    # }
    return render(request, "events/events.html")