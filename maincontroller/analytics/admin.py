from django.contrib import admin
from .models import *
# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'vacancy_name',
        'posted_date',
        'website_name',
        'effectivness',
    ]
    list_display_links = [
        'vacancy_name',
    ]
    list_filter = [
        'posted_date',
        'website_name',
    ]
    search_fields = [
        'website_name',
        'vacancy_name',
    ]

class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name'
    ]
    list_display_links = [
        'category_name'
    ]
    list_filter = [
        'category_name'
    ]
    search_fields = [
        'category_name'
    ]

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(WorkCategory, WorkCategoryAdmin)
