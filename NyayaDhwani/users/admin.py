from django.contrib import admin
from . models import (Lawyers,Clients,Profile)
# Register your models here.

admin.site.register(Lawyers)
admin.site.register(Clients)
admin.site.register(Profile)
