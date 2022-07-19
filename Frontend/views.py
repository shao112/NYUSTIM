from django.shortcuts import render

# Create your views here.
# 首頁
def index(request):
    # news = News.objects.all().order_by('id')
    # context = {
    #     'news':news
    # }
    return render(request, "index/index.html")