
from web_app.models import Posts, PostLikes
from django.contrib.auth.models import User

def like(user, post):

    try:
        liked = PostLikes.objects.get(user=user, post=post) #if fail relation doesn't exist
        #if relationship exists (if liked, unlike)
        #unlike
        PostLikes.objects.remove(liked)
        print(user,"liked",post)

    except: #if no relationship exists (if unliked, like)
        #like
        PostLikes.objects.get_or_create(user=user, post=post)
        print(user,"unliked",post)