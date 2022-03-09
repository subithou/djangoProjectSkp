from django.contrib import admin

from home.models import profile, team

# Register your models here.
@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    pass

@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    pass