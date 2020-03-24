from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Profession(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    #Create slug to display unique model attribute for URLs
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Profession, self).save(*args, **kwargs)
    
    #String to display model appropriately when called
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    location = models.CharField(max_length=32)
    bio = models.CharField(max_length=256)
    available = models.BooleanField(default=False)

    slug = models.SlugField(unique=True)

    #Create slug to display unique model attribute for URLs
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)
    
    #String to display model appropriately when called
    def __str__(self):
        return self.user.username

class UserLinks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=32)
    link = models.URLField(unique=True)
    
    #String to display model appropriately when called
    def __str__(self):
        return self.site_name


class Section(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Create slug to display unique model attribute
    class Meta:
        unique_together = (('name', 'user'))
 
    #String to display model appropriately when called  
    def __str__(self):
        return self.name



class Tags(models.Model):
    name = models.CharField(max_length=128)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    #Ensure there are no duplicate tags under one profession
    class Meta:
        unique_together = (('name', 'profession'))

    #String to display model appropriately when called
    def __str__(self):
        return self.name


class Posts(models.Model):
    pid = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to='post_images', blank=False)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
        
    #String to display model appropriately when called
    def __str__(self):
        string = ''.join((self.title,"_",str(self.pid)))
        return string

class PostTags(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    #String to display model appropriately when called
    def __str__(self):
        return self.tag.name

class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    #Ensure User cannot like a post twice
    class Meta:
        unique_together = (('user', 'post'))

    