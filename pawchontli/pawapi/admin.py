from django.contrib import admin

# Register your models here.
from .models import Image, Association

admin.site.register(Image)
admin.site.register(Association)
