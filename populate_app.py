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
		["Mid-Century Modern","Industustrail","Nautical","Scandinavian","Bohemian","Minimalist"],
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

    sections = {
        'Joe':{
            'landscapes':{
                'north-beach':{'description':'','tags':''},
                'tenby-harbour':{'description':'','tags':''}
                },

            'cityscapes':{
                'the shard':{'description':'','tags':''},
                'big ben':{'description':'','tags':''}
                },
            },
        'Tan':{
            'Logos':{
                'design_grid':{'description':'','tags':''},
                'design_folio':{'description':'','tags':''}
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

        for section_name, posts in sections[user].items(): #loop through sections for user
            add_section(section_name, u)

    #print out the pfossions added
    print('Added Professions and Tags:')
    for p in Profession.objects.all():
        print(f'- {p}')
        for t in Tags.objects.filter(profession=p):
            print(f'\t- {t}')

    #print out each user thats been added
    print('\nAdded Users:')
    for u in User.objects.all():
        print(f'-{u}')
        for s in Section.objects.filter(user=u):
            print(f'\t- {s}')

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

def add_section(name, user):
    s = Section.objects.get_or_create(name=name, user=user)[0]
    s.save()
    return s

if __name__ == '__main__':
    print('Starting web app population script...')
    populate()