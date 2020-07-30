from django.db import models
# from account.models import User
# from common.models import CoreModel
# Create your models here.

from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)



class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)