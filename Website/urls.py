from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news, name="news"),
    path("news/<str:URLName>", views.newsDetail, name="news-detail"),
    path("shop", views.shop, name="shop"),
    path("about-us", views.aboutUs, name="about-us"),
    path("contact", views.contact, name="contact"),
    # path("redirect", views.facebook, name="fb"),
]