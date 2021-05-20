from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
#from django_quill.fields import QuillField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # required to avoid error when a button is used
    def get_absolute_url(self):
        #return reverse('blogpost-detail', args=(str(self.id))) <use if going to newly created page>
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="Catikia")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="Coding")
    subject = models.CharField(max_length=255)
    thought_date = models.DateField(auto_now_add=True)
    thoughts = RichTextField(blank=True, null=True)
    summary = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # required to avoid error when add thought button is used
    def get_absolute_url(self):
        return reverse('home')
