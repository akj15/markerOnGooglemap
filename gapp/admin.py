from django.contrib import admin
from .models import PointOfInterest, Country

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class PointOfInterestAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'address', 'position', 'country')

admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(Country, CountryAdmin)