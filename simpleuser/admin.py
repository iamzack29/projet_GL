from django.contrib import admin
from .models import Account
from commune.models import Commune
from announecements.models import annonce
from wilaya.models import Wilaya
from module.models import matiere
admin.site.register(Commune)
admin.site.register(annonce)
admin.site.register(Wilaya)
admin.site.register(Account)
admin.site.register(matiere)
# Register your models here.
