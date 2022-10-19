from csv import DictReader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    page_number = int(request.GET.get("page", 1))
    stations = get_list_stations()
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)
    context = {'bus_stations': page,
               'page': page}

    return render(request, 'stations/index.html', context)


def get_list_stations() -> [dict]:
    stations = []

    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as file_csv:
        reader = DictReader(file_csv)
        for row in reader:
            stations.append({'Name': row['Name'],
                             'Street': row['Street'],
                             'District': row['District']})

    return stations
