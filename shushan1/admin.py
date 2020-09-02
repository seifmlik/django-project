from django.contrib import admin
from .models import Barile,Batterie,Info,Rabbocco

# Register your models here.
admin.site.register(Batterie)
admin.site.register(Barile)
admin.site.register(Info)
admin.site.register(Rabbocco)