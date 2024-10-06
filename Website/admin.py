from django.contrib import admin
from Website.models import News, AboutUs, ShopArticle

class NewsAdmin(admin.ModelAdmin):
    pass

class AboutUsAdmin(admin.ModelAdmin):
    pass

class ShopArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ShopArticle, ShopArticleAdmin)