# Start execution here!
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'design_grid.settings')
import django
django.setup()
from web_app.models import *

def populate():

    professions = {
	"Architect":
		["Extension","Renovation","Floor Plan","Render","Modern","Brutalist","Gothic","Industrial","Landscape"],
	"Graphic Designer":
		["Logo","Font","User Interface","Publication","Art and Illustration"],
	"Artist":
		["Digital","Concept","Abstract","Realism","Cartoon","Portrait","Landscape","Cityscape","Sculpture"],
	"Fashion Designer":
		["Dress","Suit","Casual","Abstract","Womens","Mens","Day Wear","Evening Wear","Sports Wear","Swim Wear","Lingerie"],
	"Interior Designer":
		["Mid-Century Modern","Industrail","Nautical","Scandinavian","Bohemian","Minimalist"],
	"Game Developer":
		["Character Model","Asset Model","Scene","User Interface","Shaders","Animation","Level Design"],
	"Software Designer":
		["Asset Design","Wireframe Diagrams","Database Diagrams","Class Diagrams"],
    }

    users = {
        'Joe':{'username':'joesubbi', 
            'email':'random123@gmail.com', 
            'password':'password123'},
        'Tan':{'username':'tanisha89', 
            'email':'random456@gmail.com', 
            'password':'password456'}
    }

    profile = {
        'Joe':{'location':'Pembrokeshire',
            'bio':'I like games and stuff',
            'profession':'Artist',
            'available':True
        },
        'Tan':{'location':'London',
            'bio':'CS student at University of Glasgow',
            'profession':'Graphic Designer',
            'available':False,
        }

    }

    links = {
        'Joe':{
            'instagram':'https://www.instagram.com/',
            'art station':'https://www.artstation.com/'
        },
        'Tan':{
            'facebook':'https://www.facebook.com/'

        }
    }

    sections = {
        'Joe':{
            'landscapes':{
                'north-beach':{'description':'north beach tenby','profession':'Artist','tags':['Digital','Realism','Landscape'],'likes':22},
                'tenby-harbour':{'description':'tenby harbour','profession':'Artist','tags':['Abstract','Landscape'],'likes':19}
                },

            'cityscapes':{
                'the shard':{'description':'the shard -london','profession':'Artist','tags':['Cityscape'],'likes':2},
                'big ben':{'description':'','profession':'Artist','tags':['Digital','Cityscape'],'likes':0}
                },
            },
        'Tan':{
            'Logos':{
                'design_grid':{'description':'final logo for design grid','profession':'Graphic Designer','tags':['Logo'],'likes':30},
                'design_folio':{'description':'','profession':'Graphic Designer','tags':['Logo'],'likes':52}
                }
            }
        }

    #add professions and tags using the dictionary above ^
    for prof, tags in professions.items():
        p = add_profession(prof)
        for tag in tags:
            add_tag(tag, p)

    for user, details in users.items(): #loop through users
        u = add_user(details['username'], details['email'], details['password'])
        
        d = add_profile(u,  profile[user]['location'],
                            profile[user]['bio'],
                            profile[user]['profession'],
                            profile[user]['available'])
        
        for site, link in links[user].items(): #loop through links
            l = add_link(u, site, link)
        
        for section_name, posts in sections[user].items(): #loop through sections for user
            s = add_section(section_name, u)

            for post_title, post_info in posts.items():
                profession = Profession.objects.get(name=post_info['profession'])
                p = add_post(s, post_title,post_info['description'],post_info['likes'],
                    profession)

                for tag in post_info['tags']:
                    t = Tags.objects.filter(profession=profession) #find tags of the posts profession
                    t = t.filter(name=tag)[0] #find the tag with a matching name
                    add_post_tags(p, t)



    #print out the pfossions added
    print('Added Professions and Tags:')
    for p in Profession.objects.all():
        print(f'- {p}')
        for t in Tags.objects.filter(profession=p):
            print(f'\t- {t}')

    #print out each user thats been added
    print('\nAdded Users:')
    for u in User.objects.all():
        print(f'- {u}')
        for l in UserLinks.objects.filter(user=u):
            print(f'  -Link: {l}')
        for s in Section.objects.filter(user=u):
            print(f'  -Section: {s}')
            for p in Posts.objects.filter(section=s):
                print(f'\t\t- {p}')
                for t in PostTags.objects.filter(post=p):
                    print(f'\t\t\t- {t}')

def add_profession(name):
    p = Profession.objects.get_or_create(name=name)[0]
    p.save()
    return p


def add_tag(name, profession):
    t = Tags.objects.get_or_create(name=name, profession=profession)[0]
    t.save()
    return t

def add_user(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    u.save()
    return u

def add_profile(user, location, bio, profession, available):

    profession = Profession.objects.get(name=profession)
    u = UserProfile.objects.get_or_create(user=user, profession=profession)[0]
    u.location=location
    u.bio=bio
    u.available=available
    u.save()
    return u

def add_link(user, sitename, link):
    l = UserLinks.objects.get_or_create(user=user, link=link)[0]
    l.site_name=sitename
    l.save()
    return l


def add_section(name, user):
    s = Section.objects.get_or_create(name=name, user=user)[0]
    s.save()
    return s

def add_post(section, title, description, likes, profession):
    p = Posts.objects.get_or_create(section=section, title=title)[0]
    p.description = description
    p.likes=likes
    p.profession = Profession.objects.get(name=profession)
    p.save()
    return p

def add_post_tags(post, tag):
    t = PostTags.objects.get_or_create(post=post, tag=tag)[0]
    t.save()
    return t

if __name__ == '__main__':
    print('Starting web app population script...')
    populate()