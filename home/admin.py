from django.contrib import admin
from home.models import Profile,OsobDocument,DostizhDocument

class PlanAdmin(admin.ModelAdmin):
    search_fields = ('name',)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(OsobDocument)
admin.site.register(DostizhDocument)
