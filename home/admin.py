from django.contrib import admin

from home.models import auction_data, profile, team

# Register your models here.
@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    pass

@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    pass

@admin.register(auction_data)
class auctionRecord(admin.ModelAdmin):
    pass