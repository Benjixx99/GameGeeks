from django.db import models

class News(models.Model):
    ID = models.BigAutoField(primary_key=True)
    CDate = models.DateField(auto_now_add=True)
    UDate = models.DateField(auto_now=True)
    URLName = models.CharField(max_length=100, unique=True)
    Title = models.CharField(max_length=100)
    Text = models.TextField()
    ShortText = models.CharField(max_length=5000)
    AuthorName = models.CharField(max_length=50)
    ImagePath = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "News"
    
    def str(self):
        return f"{self.Title} of {self.AuthorName}"


class AboutUs(models.Model):
    ID = models.BigAutoField(primary_key=True)
    CDate = models.DateField(auto_now_add=True)
    UDate = models.DateField(auto_now=True)
    Name = models.CharField(max_length=50)
    Text = models.TextField()
    ImagePath = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "AboutUs"

    def str(self):
        return self.Name


class ShopArticle(models.Model):
    ID = models.BigAutoField(primary_key=True)
    CDate = models.DateField(auto_now_add=True)
    UDate = models.DateField(auto_now=True)
    Name = models.CharField(max_length=50)
    Text = models.TextField()
    ImagePath = models.CharField(max_length=120)
    Price = models.FloatField()

    class Meta:
        verbose_name_plural = "ShopArticles"
    
    def str(self):
        return self.Name
