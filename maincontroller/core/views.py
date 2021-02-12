from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Scrapper
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(requеst):
    context = {
        'scrappers' : Scrapper.objects.all()
    }
    return render(requеst, 'scrapper/index.html', context=context)

