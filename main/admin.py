from django.contrib import admin
from main.models import State, StateCapital, City
# Register your models here.


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbrev')


class CapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'pop')

admin.site.register(City)
admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, CapitalAdmin)
