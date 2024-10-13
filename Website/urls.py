from django.urls import path

from . import views

urlpatterns = [
    path("", views.news, name="news"),
    path("news", views.news, name="news"),
    path("news/<str:URLName>", views.newsDetail, name="news-detail"),
    path("shop", views.shop, name="shop"),
    path("about-us", views.aboutUs, name="about-us"),
    path("contact", views.contact, name="contact"),
    path("legal-notice", views.legalNotice, name="legal-notice"),
    path("data-protection", views.dataProtection, name="data-protection"),
    # path("redirect", views.facebook, name="fb"),
]