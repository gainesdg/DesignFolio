from django.contrib import admin
from web_app.models import Profession, Tags, UserProfile, Posts

class ProfessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(UserProfile)
admin.site.register(Posts)