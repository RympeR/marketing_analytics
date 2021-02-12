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


def get_status_response(address):
    url = f"http://{address}/status/"
    response = requests.request("GET", url)
    return response.json()


def send_empty_put_request(address, action, collector_type):
    url = f"http://{address}/{collector_type}/{action}/"
    try:
        response = requests.request("PUT", url)
        return response.json()
    except Exception:
        return {'status': f'put request error url -> {url}'}


def home(requеst):
    context = {
        'vacansys': Vacancy.objects.all(),
        'scrappers': Scrapper.objects.all()
    }
    return render(requеst, 'scrapper/index.html', context=context)


class GetPauseStatus(APIView):
    def get(self, request):
        id_parser = request.GET['parsers_id']
        address = Scrapper.objects.get(pk=id_parser).address
        response = get_status_response(address)
        idsActive = response['idsCollectorStatus']['is active']
        if not idsActive:
            data = {'status_pause': 'parser not active'}
            return Response(data)
        idsPaused = response['idsCollectorStatus']['is paused']
        photoPaused = response['photosCollectorStatus']['is paused']
        ic(f'\n------PAUSED {id_parser}---------')
        ic(idsPaused, photoPaused)
        ic('--------------------\n')
        if idsPaused:
            data = {'status_pause': True}
        else:
            data = {'status_pause': False}
        return Response(data)


@api_view(['POST'])
def create_parser(request):
    port = re.search(r':(\d{4})', request.POST['Ip'])
    try:
        port = port.group(1)
        address = request.POST['Ip']
    except AttributeError:
        port = '7999'
        address = request.POST['Ip'] + ':' + port
    Scrapper.objects.create(
        address=address,
        is_deleted=False,
        is_active=False,
        login=request.POST['Login'],
        password=request.POST['Password'],
        name=request.POST['Name']
    ).save()

    # try:
    #     login = request.POST['Login']
    #     address = request.POST['Ip']
    #     password = request.POST['Password']
    #     print(f'\n Parser created {request.POST}\n')
    #     command = f"bash core/deploy/core_run.sh {login} {address} {password} {port}"
    #     print(f'\n\n --- command auto core----\n\t {command}\n\n')
    #     os.system(command)
    # except Exception as e:
    #     print(e)
    #     return Response({'success': False})
    return Response({'success': True})



class GetStatusParser(APIView):
    def get(self, request):
        try:
            address_parser = Scrapper.objects.get(id=request.GET['parsers_id'])
            response = get_status_response(address_parser.address)
            
            ic(response['vacancyCollectorStatus'])
            data = {
                    'status' : response['vacancyCollectorStatus']
            }
        except Exception as e:
            ic(e)
            
            data = {
                    'status' : 'error'
            }
        return Response(data)   

