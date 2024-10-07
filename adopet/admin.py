from django.contrib import admin
from adopet.models import Tutor, Pet

class Tutors(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name',)
    list_per_page = 10
    search_fields = ('name',)
    
admin.site.register(Tutor, Tutors)

class Pets(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'size',)
    list_display_links = ('id', 'name',)
    list_per_page = 10
    search_fields = ('name',)
    
admin.site.register(Pet, Pets)