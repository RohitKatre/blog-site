from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="img/")
    date = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title


# class Comments(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)
#     comment = models.CharField(max_length = 512)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(slef):
#         return self.user.username + "  " + self.comment

class Comment(models.Model):
    post = models.ForeignKey('Article', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
