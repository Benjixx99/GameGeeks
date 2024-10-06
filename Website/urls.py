from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news, name="news"),
    path("news/<str:URLName>", views.newsDetail, name="news_detail"),
    path("about-us", views.aboutUs, name="about_us"),
    path("contact", views.contact, name="contact"),
    # path("redirect", views.facebook, name="fb"),
]