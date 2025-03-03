from django.contrib import admin
from MedApp.models import *
#asterick(*)means all
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(ward)
admin.site.register(staff)
admin.site.register(appointment)
admin.site.register(cont)
