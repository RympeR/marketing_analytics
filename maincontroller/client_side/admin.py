from django.contrib import admin

# Register your models here.
from .models import Client, ClientWork, ClientWorkPreferences


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


admin.site.register(Client, ClientAdmin)
admin.site.register(ClientWork)
admin.site.register(ClientWorkPreferences)
