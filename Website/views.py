from django.shortcuts import render, redirect
from django.http import HttpResponse

from Website.models import News, ShopArticle, AboutUs

def index(request):
    return render(request, "index.html")

def news(request):
    allNews = News.objects.all().order_by("-CDate")
    context = { "allNews" : allNews }
    return render(request, "news.html", context)

def newsDetail(request, URLName):
    news = News.objects.get(URLName=URLName)
    context = { "news" : news }
    return render(request, "news-detail.html", context)

def shop(request):
    shopArticle = ShopArticle.objects.all().order_by("-CDate")
    context = { "shopArticle" : shopArticle }
    return render(request, "shop.html", context)

def aboutUs(request):
    allAboutUs = AboutUs.objects.all().order_by("CDate")
    context = { "allAboutUs" : allAboutUs }
    return render(request, "about-us.html", context)

def contact(request):
    return render(request, "contact.html")




# TODO: Find a solution for this!
def facebook(request):
    return redirect("www.facebook.com", permanent=True)
