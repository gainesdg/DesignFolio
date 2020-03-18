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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    location = models.CharField(max_length=32)
    bio = models.CharField(max_length=256)
    available = models.BooleanField(default=False, null=False)
    link1 = models.URLField(blank=True)
    link2 = models.URLField(blank=True)
    link3 = models.URLField(blank=True)
    
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Section(models.Model):
    name = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=128)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'profession'))

    def __str__(self):
        return self.name


class Posts(models.Model):
    pid = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to='post_images', blank=True)
    title = models.CharField(max_length=128)
    descriptiuon = models.CharField(max_length=512)
    likes = models.IntegerField(default=0)

    
    def __str__(self):
        string = ''.join((self.title,"_",str(self.pid)))
        return string

class PostTags(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.name

