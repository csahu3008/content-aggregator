from django.db import models
from django.utils.timezone import now
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Category(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
         return self.title
    class Meta:
        verbose_name_plural='Category'
class News(models.Model):
    headline=models.CharField(max_length=400)
    description=models.TextField(max_length=400,null=True)
    url=models.URLField(max_length=400,null=True)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    dislikes=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='dislike')
    url_image=models.URLField(max_length=500,null=True)
    picture=models.ImageField(max_length=400,upload_to='images/%Y/%m/%d/',default='images/default.jpg')
    author=models.CharField(max_length=400,null=True,blank=True)
    date_published=models.DateField(auto_now=True)
    categories=models.ManyToManyField(Category,blank=True)
    class Meta:
        verbose_name_plural='News'
        ordering=['-id',]
    def __str__(self):
        return 'article {} published on {}'.format(self.headline,self.date_published)
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    title=models.CharField(max_length=200)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,default=None)
    news=models.ForeignKey(News,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "comment {} was added in {}".format(self.title,self.news)
