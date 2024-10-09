from django.contrib import admin
from adopet.models import Tutor, Shelter, Pet

class Tutors(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name',)
    list_per_page = 10
    search_fields = ('name',)
    ordering = ('name',)
    
admin.site.register(Tutor, Tutors)

class Shelters(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    list_per_page = 10
    search_fields = ('name',)
    ordering = ('name',)
    
admin.site.register(Shelter, Shelters)
    
class Pets(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'size',)
    list_display_links = ('id', 'name',)
    list_per_page = 10
    search_fields = ('name',)
    ordering = ('name',)
    
admin.site.register(Pet, Pets)

