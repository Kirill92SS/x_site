import re
from unicodedata import category
from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET(1), null=True)

    def __str__(self):
        return self.title
    
    def get_content(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    category = models.CharField(max_length=255)

    def get_category(self):
        return reverse('category', kwargs={'cat_id': self.pk})