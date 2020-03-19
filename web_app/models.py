from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Profession(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Profession, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=64, unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)
    def __str__(self):
        return self.user_name
class Section(models.Model):
    section_id = models.AutoField(unique=True)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name
"""

class Tags(models.Model):
    name = models.CharField(max_length=128)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""
class Posts(models.Model):
    post_id = models.AutoField(unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='post_images', blank=True)
    title = models.CharField(max_length=128)
    descriptiuon = models.CharField(max_length=512)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.user.username
"""
