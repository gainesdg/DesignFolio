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

    post = {
    "id":1,
    "section":"Stars"
    }

    #add professions and tags using the dictionary above ^
    for prof, tags in professions.items():
        p = add_profession(prof)
        for tag in tags:
            add_tag(tag, p)

    #print out the pfossions added
    for p in Profession.objects.all():
        print(f'- {p}')
        for t in Tags.objects.filter(profession=p):
            print(f'\t- {t}')

def add_profession(name):
    p = Profession.objects.get_or_create(name=name)[0]
    p.save()
    return p


def add_tag(name, profession):
    t = Tags.objects.get_or_create(name=name, profession=profession)[0]
    t.save()
    return t


if __name__ == '__main__':
    print('Starting web app population script...')
    populate()