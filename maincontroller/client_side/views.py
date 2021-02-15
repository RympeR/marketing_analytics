from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .psycopg_models import *
from .models import *

# Create your views here.


def where_add(query):
    if 'where' not in query:
        query += '\nwhere'
    return query


def add_and_case(request, query, param_name, field_name, empty=False, str_=True):
    if empty:
        if request.form[param_name] != 'empty':
            query = where_add(query)
            param = request.form[param_name]
            if query.split('\n')[-1].strip() != 'where':
                if str_:
                    query += f"\nand {field_name}= '{param}'"
                else:
                    query += f"\nand {field_name}= {param}"
            else:
                if str_:
                    query += f"\n{field_name}= '{param}'"
                else:
                    query += f"\n{field_name}= {param}"
    else:
        if request.form[param_name] != '':
            query = where_add(query)
            param = request.form[param_name]
            if query.split('\n')[-1].strip() != 'where':
                if str_:
                    query += f"\nand {field_name}= '{param}'"
                else:
                    query += f"\nand {field_name}= {param}"
            else:
                if str_:
                    query += f"\n{field_name}= '{param}'"
                else:
                    query += f"\n{field_name}= {param}"
    return query


def get_cars(request, login, password):
    try:
        query = '''select
                    modeltype, releasdata,
                    climatcontroltype,
                    audiosystemtype,
                    price, fuel_type,
                    fuelconsumption, colore,
                    enginevolume
                    from car
                    join specification using(specification_id)
                    join color using(color_id)
                    join audiosystem using(audiosystem_id)
                    join transmissiontype using(transmissiontype_id)
                    join climatcontrol using(climatcontrol_id)
                    join fueltype using(fueltype_id)'''
        query = add_and_case(request, query, 'modeltype', 'modeltype')
        query = add_and_case(request, query, 'releasdata', 'releasdata')
        query = add_and_case(request, query, 'climatcontroltype',
                             'climatcontrol_id', empty=True, str_=False)
        query = add_and_case(request, query, 'audiosystemtype',
                             'audiosystem_id', empty=True, str_=False)
        query = add_and_case(request, query, 'price', 'price', str_=False)
        query = add_and_case(request, query, 'fuel_type',
                             'fueltype_id', empty=True, str_=False)
        query = add_and_case(
            request, query, 'fuelconsumption', 'fuelconsumption')
        query = add_and_case(request, query, 'colore',
                             'color_id', empty=True, str_=False)
        query = add_and_case(request, query, 'enginevolume',
                             'enginevolume', str_=False)
        query += ';'
        print(query)
        result = execute_select_query(login, password, query)

    except Exception as e:
        print(e)
        query = '''select 
                    modeltype, releasdata,
                    climatcontroltype,
                    audiosystemtype,
                    price, fuel_type,
                    fuelconsumption, colore,
                    enginevolume
                    from car
                    join specification using(specification_id)
                    join color using(color_id)
                    join audiosystem using(audiosystem_id)
                    join transmissiontype using(transmissiontype_id)
                    join climatcontrol using(climatcontrol_id)
                    join fueltype using(fueltype_id);    
                '''
        result = execute_select_query(login, password, query)
    return result


def registration(request):
    shutdown_session(request)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client_ = Client(
                contact_details=form.cleaned_data['contact_details'],
                full_name=form.cleaned_data['full_name'],
                login=form.cleaned_data['login'],
                passw=form.cleaned_data['passw'],
                date_of_registration=datetime.today().strftime('%Y-%m-%d')
            )
            client_.save()
            request.session['username'] = request.POST['login']
            request.session['password'] = request.POST['passw']
            username = request.POST['login']
            password = request.POST['passw']
            try:
                query = f"""SELECT "ID_Client" FROM "Client" WHERE login = '{username}' AND passw = '{password}' ;"""
                print(query)
                request.session['login'] = execute_select_query(
                    'tourism_guest', 'guest', query, f_all=False)[0]
                print(request.session['login'])
                if request.session['login'] > 0:
                    request.session['username'] = username
                    role = 'tourism_client:client'
                    return redirect(client, username=request.session['username'])
            except Exception as e:
                print(e)
                return render(request, 'tourism/registration.html')
    context = {
        "form": ClientForm
    }
    return render(request, 'tourism/registration.html', context=context)


def shutdown_session(request):
    request.session.clear()


def login(request):
    global role

    if 'login' in request.session.keys() and 'username' in request.session.keys():
        print(request.session.items())
        if request.session['login'] == 'staff':
            role = 'tourism_staff:staff'
            return redirect(manager, username=request.session['username'])
        elif request.session['login']:
            role = 'tourism_client:client'
            return redirect(client, username=request.session['username'])
    if request.method == 'POST':
        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        username = request.POST['username']
        password = request.POST['password']
        try:
            query = f"""SELECT role_user FROM "Staff" WHERE login = '{username}' AND passw = '{password}' ;"""
            request.session['login'] = execute_select_query(
                'tourism_guest', 'guest', query, f_all=False)[0].replace('\n', '')
            print(request.session['login'])
            if request.session['login'] == 'director':
                role = 'tourism_director:director'
                print(request.session['username'])
                return redirect(director, username=request.session['username'])
            elif request.session['login']:
                role = 'tourism_client:client'
                return redirect(client, username=request.session['username'])
        except Exception as e:
            print(e)
            try:
                query = f"""SELECT "ID_Client" FROM "Client" WHERE login = '{username}' AND passw = '{password}' ;"""
                print(query)
                request.session['login'] = execute_select_query(
                    'tourism_guest', 'guest', query, f_all=False)[0]
                print(request.session['login'])
                if request.session['login'] > 0:
                    request.session['username'] = username
                    role = 'tourism_client:client'
                    return redirect(client, username=request.session['username'])
            except Exception as e:
                print(e)
                return render(request, 'tourism/login.html')

    return render(request, 'tourism/login.html')


def logout(request):
    request.session.clear()
    return redirect(login)


def generate_search_query(request):
    query = '''
    '''
    data = execute_select_query('postgres', '1111', query)
    return data


def index(request):
    return render(request, 'main.html')


def profile(request):
    if 'username' not in request.session or request.session['username'] != username:
        return render(request, 'tourism/login.html')
    return render(request, 'client/profile.html')


def search(request):
    data = {}
    if request.method == 'POST':
        data = generate_search_query(request)
    context = {
        'data': data
    }
    return render(request, 'client/search.html', context=context)


def stats(request):
    if 'username' not in request.session or request.session['username'] != username:
        return render(request, 'tourism/login.html')
    return render(request, 'client/stats.html')
