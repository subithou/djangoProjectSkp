from django.contrib import admin

from login.models import auction_admin

# Register your models here.
@admin.register(auction_admin)
class auctionAdmin(admin.ModelAdmin):
    pass