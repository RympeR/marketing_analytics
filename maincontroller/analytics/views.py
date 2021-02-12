from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Scrapper, Vacancy
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import re
import os
from icecream import ic