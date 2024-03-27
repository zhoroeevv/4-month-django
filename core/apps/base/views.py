from django.shortcuts import render
from apps.base.models import InfoUser,Secondary,Testim
from apps.secondary.models import News
# Create your views here.
def index(request):
    infouser = InfoUser.objects.latest("id")
    secondary = Secondary.objects.latest("id")
    testim  = Testim.objects.all()
    news = News.objects.all()
    return render(request, "index.html",locals())

def news_detail(request,id):
    news = News.objects.get(id=id)
    return render(request,"blog-details.html", locals())

