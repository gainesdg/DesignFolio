import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'design_grid.settings')
import django
django.setup()
from web_app.models import *
from django.contrib.auth.hashers import make_password

def populate():
    #MODEL DETAILS
    #professions and tags
    professions = {
        "Architect":
            ["Extension","Renovation","Floor Plan","Render","Modern","Brutalist","Gothic","Industrial","Landscape"],
        "Graphic Designer":
            ["Logo","Font","User Interface","Publication","Art and Illustration"],
        "Artist":
            ["Digital","Concept","Abstract","Realism","Cartoon","Portrait","Landscape","Cityscape","Sculpture", "Sketch"],
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
        'Joe':{
            'firstname':'Joe',
            'lastname':'Subbiani',
            'username':'JoeSubbi',
            'email':'joe.subbiani@gmail.com',
            'password':'password123'
            },
        'Tan':{
            'firstname':'Tanisha',
            'lastname':'Sarkar',
            'username':'Tanisa89',
            'email':'tanisha.s@gmail.com',
            'password':'password123'
            },
        'Kam':{
            'firstname':'Kameron',
            'lastname':'Eralp',
            'username':'kam33',
            'email':'eralp2001@gmail.com',
            'password':'password123'
            },
        'Dyl':{
            'firstname':'Dylan',
            'lastname':'gaines',
            'username':'dG',
            'email':'gaines.a@gmail.com',
            'password':'password123'
            },
        'Dav':{
            'firstname':'Dave',
            'lastname':'Filoni',
            'username':'Dave44',
            'email':'ww66@gmail.com',
            'password':'password123'
            }
    }

    profile = {
        'Joe':{
            'picture':'profile_images/Helmet_Concept_z2uC6nn.PNG',
            'location':'Pembroke',
            'bio':'I like to make stuff',
            'profession':'Artist',
            'available':True,
            },
        'Tan':{
            'picture':None,
            'location':'London',
            'bio':'Graphic Designer',
            'profession':'Graphic Designer',
            'available':True,
            },
        'Kam':{
            'picture':None,
            'location':'Glasgow',
            'bio':'Computer Science Student at the University of Glasgow',
            'profession':'Software Designer',
            'available':False,
            },
        'Dyl':{
            'picture':None,
            'location':'Calafornia',
            'bio':'US Transfer at Uni of Glasgow',
            'profession':'Interior Designer',
            'available':False,
            },
        'Dav':{
            'picture':'profile_images/Helmet_Concept.PNG',
            'location':'Hollywood',
            'bio':'Creator of The Mandalorian. Successor to George Lucas',
            'profession':'Game Developer',
            'available':True,
            }
    }

    links = {
        'Joe':{
            'instagram':'https://www.instagram.com/joesubbi/',
            'art station':'https://www.artstation.com/',
            'newgrounds':'https://joesubbi.newgrounds.com/',
            'linked in':'https://www.linkedin.com/in/joe-subbiani-1b326a198/',
            'facebook':'https://www.facebook.com/JoeSubbi7',
        },
        'Tan':{
            'instagram':'https://www.instagram.com/',
        },
        'Kam':{
        },
        'Dyl':{
            'facebook':'https://www.facebook.com/',
        },
        'Dav':{
            'SW':'https://www.starwars.com/',
            'instagram':'https://www.instagram.com/venamis/',
        },
    }

    posts = {
        'Mandolorian Comission':{
            'picture':'post_images/Commision_Fabric.png',
            'description':'Commision I did for someone\'s some custom mandolorian armour',
            'profession':'Artist',
            'tags':['Digital','Concept']
            },
        'OctoCat':{
            'picture':'post_images/OctoCat_2.png',
            'description':'Hackathon github challenge to redraw the github octocat mascot',
            'profession':'Artist',
            'tags':['Digital','Cartoon','Landscape']
         },
        'Powerpuff girl':{
            'picture':'post_images/Sam_B-Day_Card.png',
            'description':'Birthday card design for a friend. stylised power puff girl.',
            'profession':'Graphic Designer',
            'tags':['Art and Illustration']
            },
        'GUSEC Logo':{
            'picture':'post_images/Artboardx.png',
            'description':'Logo for the Univeristy of Glasgow Security Society',
            'profession':'Graphic Designer',
            'tags':['Logo']
            },
        'Alien':{
            'picture':'post_images/Alien_hall.png',
            'description':'Concept for a new alien game in the works ;)',
            'profession':'Game Developer',
            'tags':['Character Model','Asset Model','Scene']
            },
        'Alien Sketch':{
            'picture':'post_images/Alien.png',
            'description':'Practicing pencil sketch with a xenomorph',
            'profession':'Artist',
            'tags':['Concept','Digital','Sketch']
            },
        'Alita: Battle Angel':{
            'picture':'post_images/Alita.png',
            'description':'Just some fun fan art. Practicing hair. Still a long way to go',
            'profession':'Artist',
            'tags':['Digital']
            },
        'Spartan Concept':{
            'picture':'post_images/Spartan.png',
            'description':'Practing shadows in photoshop.',
            'profession':'Graphic Designer',
            'tags':['Art and Illustration']
            },
        'Physics Poster':{
            'picture':'post_images/Poster_Final.jpg',
            'description':'Poster to uploaded to University of glasgow Moodle Page',
            'profession':'Software Designer',
            'tags':['Asset Design']
            }
    }

    sections = {
        'Joe':{
            'Concept Art':['Mandolorian Comission'], 
            'Competitions':['OctoCat'], 
            'Practice':['Alien Sketch','Alita: Battle Angel']
            },
        'Tan':{
            'Practice':['Powerpuff girl', 'Spartan Concept'],
            'Logos':['GUSEC Logo']
            },
        'Kam':{
            'Moodle Development':['Physics Poster']
            },
        'Dyl':{
            'section':[]
            },
        'Dav':{
            'Aliens Game':['Alien']
            },
    }
    
    likes = {
        'Mandolorian Comission':['Tan','Dav'],
        'OctoCat':['Tan','Kam'],
        'Alien Sketch':['Tan','Kam','Dyl','Dav'],
        'Alita: Battle Angel':['Kam','Dyl'],
        'Powerpuff girl':['Joe','Kam'],
        'Spartan Concept':['Joe'],
        'GUSEC Logo':['Dyl','Joe','Dav','Kam'],
        'Physics Poster':['Joe','Tan'],
        'Alien':['Joe','Kam','Tan'],
    }

    #PROCESS OF CALLING FUNCTIONS TO ADD MODEL OBJECTS

    #add professions and tags using the dictionary above ^
    for prof, tags in professions.items():
        p = add_profession(prof)
        for tag in tags:
            add_tag(tag, p)

    for user in users: #loop through names. These names identify users, profiles and links etc.
        userDetails = users[user]
        userProfile = profile[user]

        u = add_user(userDetails) #dictionary of user details
        p = add_profile(u, userProfile) #user object, dictionary of profile details

        for site, link in links[user].items():
            l = add_link(u, site, link) #user model object, site name and link to site

        for section, post_list in sections[user].items():
            s = add_section(u, section) #user model object, section name

            for post in post_list:
                p = add_post(post, s, posts[post]) #title, section model object, dictionary of post details
                for tag in posts[post]['tags']:
                    t = add_post_tag(p, tag) #post object, tag name

                for user_like in likes[post]:
                    add_like(p, User.objects.get(username = users[user_like]['username']))#post model object, user model object

    #CONSOL OUTPUT TO SHOW SUCCESSFUL ADDITIONS TO THE DATABASE
    #print out the pfossions added
    print('Added Professions and Tags:')
    for p in Profession.objects.all():
        print(f'{p}')
        for t in Tags.objects.filter(profession=p):
            print(f' └─ {t}')
    
    print('Added Users:')
    for u in User.objects.all():
        print(f'{u.first_name} {u.last_name}\n{u}')
        print(' └─ Links:')
        for l in UserLinks.objects.filter(user=u):
            print(f'     └─ {l}')
        print(' └─ Sections and Posts:')
        for s in Section.objects.filter(user=u):
            print(f'     └─ {s}')
            for p in Posts.objects.filter(section=s):
                l = len(PostLikes.objects.filter(post=p))
                print(f'        └─ {p} Likes: {l}')
                for t in PostTags.objects.filter(post=p):
                    print(f'           └─ {t}')


#FUNCTIONS TO ADD MODEL OBJECT
#CATEGORIES AND TAGS
def add_profession(name):
    #Create object
    p = Profession.objects.get_or_create(name=name)[0]
    p.save()
    return p

def add_tag(name, profession):
    #Create object
    t = Tags.objects.get_or_create(name=name, profession=profession)[0]
    t.save()
    return t

#USERS, SECTIONS AND POSTS
def add_user(user):
    #Get details
    first_name = user['firstname']
    last_name = user['lastname']
    username = user['username']
    email = user['email']
    password = make_password(user['password'])
    #Create object
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.password=password
    u.first_name=first_name
    u.last_name=last_name
    u.save()
    return u

def add_profile(user, profile):
    #Get details
    picture = profile['picture']
    location = profile['location']
    bio = profile['bio']
    profession = Profession.objects.get(name=profile['profession'])
    available = profile['available']
    #Create object
    p = UserProfile.objects.get_or_create(user=user, profession=profession)[0]
    p.picture = picture
    p.location=location
    p.bio=bio
    p.available=available
    p.save()
    return p

def add_link(user, site, link):
    #Create object
    l = UserLinks.objects.get_or_create(user=user, link=link)[0]
    l.site_name=site
    l.save()
    return l

def add_section(user, name):
    #Create object
    s = Section.objects.get_or_create(name=name, user=user)[0]
    s.save()
    return s

def add_post(title, section, details):
    #Get post details
    picture = details['picture']
    description = details['description']
    profession = Profession.objects.get(name=details['profession'])
    #Create object
    p = Posts.objects.get_or_create(section=section, title=title)[0]
    p.description=description
    p.profession=profession
    p.picture=picture
    p.save()
    return p

def add_post_tag(post, tag):
    #Get tag details
    tag = Tags.objects.get(name=tag, profession=post.profession)
    
    #Create object
    t = PostTags.objects.get_or_create(post=post, tag=tag)[0]
    t.save()
    return t

def add_like(post, user):
    l = PostLikes.objects.get_or_create(user=user, post=post)[0]
    l.save()
    return l


#START POPULATION SCRIPT
if __name__ == '__main__':
    print('Starting web app population script...')
    populate()