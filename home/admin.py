from django.contrib import admin
from home.models import Profile

class PlanAdmin(admin.ModelAdmin):
    search_fields = ('name',)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
admin.site.register(Profile,ProfileAdmin)
