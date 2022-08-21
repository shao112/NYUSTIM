from django.shortcuts import render
from .models import Members, Competition, Appointment, Events
from django.http import JsonResponse
# 分頁
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
# Form
from .forms import AppointmentForm

# Create your views here.
@csrf_exempt
def DataTransform(request,dbtype):

    switch_db = {
        "members":Members,
        "competition":Competition,
        "appointment":Appointment,
        "events":Events
    }
    getdb = switch_db.get(dbtype)

    datalist = []
    if dbtype ==None:
        return JsonResponse({"error":"請求失敗"})
    else:        
        getdata = getdb.objects.all()
        for one_data in getdata:
            if getdb == Members:
                # 可能之後有選項的都要改成 type
                one_data.position = one_data.get_position_display()
                print(one_data.position)
            data = one_data.to_dict()
            print("-------------------")
            print(data)
            datalist.append(data)
        print(datalist)
    return JsonResponse(datalist, safe=False)

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
    # 顯示 6 筆資料
    paginator = Paginator(competition, 6)
    # 獲取 url 中的頁碼，比如第一頁，我們需要在url末尾中新增 ?page=1
    page = request.GET.get('page')
    # 獲取相應的頁碼的資料，比如page=1，第一頁，這裡獲取得到第一頁的資料內容
    competition = paginator.get_page(page)
    # 獲取一共分出來了多少頁，前端展示所有頁碼數的時候需要用到該數
    print("總共有",paginator.num_pages,"頁")
    print("多少資料",paginator.object_list)
    print(competition.paginator.page_range)

    context = {
        'competition':competition
    }

    return render(request, "competition/competition.html", context)

# 預約友誼賽
def appointment(request):


    form = AppointmentForm()

    context = {
        'form':form
    }

    return render(request, "appointment/appointment.html", context)

# 活動公告
def events(request):
    
    events = Events.objects.all().order_by('id')
    
    # 顯示 6 筆資料
    paginator = Paginator(events, 10)
    # 獲取 url 中的頁碼，比如第一頁，我們需要在url末尾中新增 ?page=1
    page = request.GET.get('page')
    # 獲取相應的頁碼的資料，比如page=1，第一頁，這裡獲取得到第一頁的資料內容
    events = paginator.get_page(page)
    # 獲取一共分出來了多少頁，前端展示所有頁碼數的時候需要用到該數
    print("總共有",paginator.num_pages,"頁")
    print("多少資料",paginator.object_list)
    print(events.paginator.page_range)

    context = {
        'events':events
    }

    return render(request, "events/events.html", context)