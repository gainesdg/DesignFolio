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


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=128, unique=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_name


class Section(models.Model):
    name = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=128)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)


class Posts(models.Model):
    post_id = models.IntegerField()
    category = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    descriptiuon = models.CharField(max_length=512)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags)

