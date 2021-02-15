from django.contrib import admin
from .models import *
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'login',
        'work_stage',
        'salary_preference'
    ]
    list_display_links = [
        'login'
    ]
    list_filter = [
        'work_stage'
    ]
    search_fields = [
        'login'
    ]


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
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientWork)
admin.site.register(ClientWorkPreferences)
admin.site.register(City)
