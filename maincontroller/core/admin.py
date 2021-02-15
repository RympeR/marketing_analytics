from django.contrib import admin
from .models import *
# Register your models here.


class ScrapperAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'is_deleted',
        'login'
    ]
    list_display_links = [
        'name'
    ]
    list_filter = [
        'is_deleted',
    ]
    search_fields = [
        'name'
    ]


admin.site.register(Scrapper, ScrapperAdmin)

admin.site.register(City)
