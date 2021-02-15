from django.urls import path, include
from .views import *

app_name = 'core'


urlpatterns = [
    path('', home, name='scrapper-home'),
    path('create-parser/', create_parser, name='create_parser'),
    path('action-scrapper/', ParserAction.as_view(), name='action_scrapper'),
    path('pause-status/', GetPauseStatus.as_view(), name='pause_status'),
    path('status/', GetStatusParser.as_view(), name='status'),
    path('set-filter-settings/', SetSettingsFiltersParser.as_view(), name='set_filter_settings'),
]
