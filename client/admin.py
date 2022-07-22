from django.contrib import admin

from .models import *

admin.site.register(Client)
admin.site.register(Region)
admin.site.register(Ville)
admin.site.register(Médicaux)
admin.site.register(Chirurgicaux)
admin.site.register(Sexe)
admin.site.register(Vaccin)
admin.site.register(Allergies)

