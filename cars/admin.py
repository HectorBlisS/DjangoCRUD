from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
	list_display = ['id','modelo','fecha','propietario']

admin.site.register(Car, CarAdmin)