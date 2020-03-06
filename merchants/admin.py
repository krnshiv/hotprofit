from django.contrib import admin

from .models import Merchant

class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id','name','sublocality','city','mvp','last_active')
    list_display_links = ('id','name')
    list_filter = ('sublocality','city')
    list_editable = ('mvp',)
    search_fields = ('name','sublocality','city')
    list_per_page = 25

admin.site.register(Merchant, MerchantAdmin)
