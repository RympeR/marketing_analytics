from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Scrapper, Vacancy, City, WorkCategory
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
        'vacancys': WorkCategory.objects.all(),
        'scrappers': Scrapper.objects.all(),
        'cities': City.objects.all(),
    }
    return render(requеst, 'scrapper/index.html', context=context)


class GetPauseStatus(APIView):
    def get(self, request):
        id_parser = request.GET['parsers_id']
        address = Scrapper.objects.get(pk=id_parser).address
        response = get_status_response(address)
        idsActive = response['vacancyCollectorStatus']['is active']
        if not idsActive:
            data = {'status_pause': 'parser not active'}
            return Response(data)
        vacancysPaused = response['vacancyCollectorStatus']['is paused']
        ic(f'\n------PAUSED {id_parser}---------')
        ic(vacancysPaused)
        ic('--------------------\n')
        if vacancysPaused:
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
            address_parser = Scrapper.objects.get(pk=request.GET['parsers_id'])
            response = get_status_response(address_parser.address)
            parserStatus = 'Активен' if response['vacancyCollectorStatus']['is active'] == True else 'Выключен'
            parserCity = response['vacancyCollectorStatus']['filter']['city_name']
            parserWebsite = response['vacancyCollectorStatus']['filter']['website']
            parserThread = response['vacancyCollectorStatus']['settings']['number of threads']
            parserStageFrom = response['vacancyCollectorStatus']['filter']['stage_from']
            parserStageTo = response['vacancyCollectorStatus']['filter']['stage_to']
            vacancysInPack = response['vacancyCollectorStatus']['filter']['vacancys in pack']
            parserParsedVacancys = response['vacancyCollectorStatus']['collected vacancys']
            pausedStatus = response['vacancyCollectorStatus']['is paused']
            activeStatus = response['vacancyCollectorStatus']['is active']
            parserVacancy = response['vacancyCollectorStatus']['vacancy']
            ic(response['vacancyCollectorStatus'])
            if isinstance(parserCity, list):
                if len(parserCity) != 1:
                    for city in parserCity:
                        parserCity = ''
            data = {
                'isActive': activeStatus,
                'parserStatus': parserStatus,
                'isPaused': pausedStatus,
                'parserWebsite': parserWebsite,
                'parserCity': parserCity,
                'parserThread': parserThread,
                'parserStageFrom': parserStageFrom,
                'parserStageTo': parserStageTo,
                'parserParsedVacancys': parserParsedVacancys,
                'vacancysInPack': vacancysInPack,
                'parserVacancy': parserVacancy,
                'status': 'success'
            }
        except Exception as e:
            ic(e)

            data = {
                'status': 'error'
            }
        return Response(data)


class SetSettingsFiltersParser(APIView):
    def get(self, request):
        vacansy = request.GET['Vacansy']
        city = request.GET['City']
        website = request.GET['Website']
        thread_amount = request.GET['Thread']
        amount_vacancy_in_pack = request.GET['Folder']
        id_parser = request.GET['ID']
        pack_amount = request.GET['PackAmount']
        print(f'\n got values\n \t{request.GET} \n')
        print(f'Parser id->{id_parser}')

        ip_port = Scrapper.objects.get(pk=id_parser).address

        url = f"http://{ip_port}/Vacancys/set_settings/"
        if pack_amount != '':
            data = {
                "vacancys in pack": amount_vacancy_in_pack,
                "number of threads": thread_amount,
                "pack amount": pack_amount,
            }
        else:
            data = {
                "vacancys in pack": amount_vacancy_in_pack,
                "number of threads": thread_amount,
            }
        print(f"Set settings {data}")

        if city == '':
            city = list(City.objects.all().values())
        else:
            city = [city]
        try:
            response = requests.request("PUT", url, data=data)
            print(response.status_code)
        except Exception:
            return HttpResponse(content={
                'success': False,
                'message': 'Ошибка установки настроек'
            })

        url = f"http://{ip_port}/Vacancys/set_filter/"
        data = {
            "vacansy": vacansy,
            "website": website,
            "city_id": city
        }

        print(f"Set ids filter {data}\n\t{url}")

        try:
            response = requests.request("PUT", url, data=data)
            print(response.status_code)
        except Exception:
            return HttpResponse(content={
                'success': False,
                'message': 'Ошибка установки фильтров id парсера'
            })

        return Response({
            'success': True,
            'message': 'Фильтр настроен и перезапущен'
        })


class ParserAction(APIView):
    def post(self, request):
        id_parser = request.POST['parsers_id']
        print(id_parser)
        address = Scrapper.objects.get(pk=id_parser).address
        response = get_status_response(address)
        print(response)
        IdStatus = response['vacancyCollectorStatus']
        print(request.POST)

        if 'run' == request.POST['action']:
            print('\n RUN PARSERS\n')
            if not IdStatus['is active']:
                Scrapper.objects.filter(pk=id_parser).update(is_active=True)
                response = send_empty_put_request(address, 'run', 'Ids')

        if 'pause' == request.POST['action']:
            print('\n PAUSE PARSERS\n')
            if not IdStatus['is paused']:
                response = send_empty_put_request(address, 'pause', 'Ids')

        if 'unpause' == request.POST['action']:
            print('\n UNPAUSE PARSERS\n')
            if IdStatus['is paused']:
                response = send_empty_put_request(address, 'unpause', 'Ids')

        if 'stop' == request.POST['action']:
            print('\n STOP PARSERS\n')
            if IdStatus['is active']:
                Scrapper.objects.filter(pk=id_parser).update(is_active=False)
                response = send_empty_put_request(address, 'stop', 'Ids')
        return Response({'status': 'success'})
