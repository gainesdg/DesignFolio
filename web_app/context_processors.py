from web_app.models import Profession

def professions(request):
    return {
        'professions': Profession.objects.all()
    }