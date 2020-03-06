from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','name','brand','posted','is_valid','newprice','category','merchant','tags')
    list_display_links = ('id','name')
    list_filter = ('merchant','category','brand','tags')
    list_editable = ('is_valid',)
    search_fields = ('name','description','category','brand','merchant')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)
