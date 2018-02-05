from django.contrib import admin

# Register your models here.

from .models import Musicion,Album,Person

admin.site.register(Musicion)
admin.site.register(Album)
admin.site.register(Person)