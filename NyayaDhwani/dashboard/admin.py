from django.contrib import admin
from .models import register_case,lawyer_type,case

admin.site.register(register_case)
admin.site.register(case)
admin.site.register(lawyer_type)

# Register your models here.
