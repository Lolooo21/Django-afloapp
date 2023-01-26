from django.contrib import admin

from .models import Eleve, Formateur, Formation, Information

# Register your models here.

admin.site.register(Formation)
admin.site.register(Formateur)
admin.site.register(Information)
admin.site.register(Eleve)
