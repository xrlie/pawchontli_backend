from django.contrib import admin

# Register your models here.
from .models import  Association, Adopter, Pet


admin.site.register(Association)
admin.site.register(Adopter)
admin.site.register(Pet)
