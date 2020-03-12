from django.shortcuts import render
from .model import Com
from .model import ComCost
from .forms import ComForm
from datetime import date
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from xml.etree import ElementTree as ET
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q


#@login_required
def count_page(request):

    today = date.today()

    if request.method == "POST":
        com_cost = ComCost.objects.latest('id')
        com_last = Com.objects.latest('id')

        print(request.POST)
        # get data
        electric = request.POST['electric']
        water_h = request.POST['water_h']
        water_c = request.POST['water_c']
        waste = int(water_h) + int(water_c)
        waste_count = int(waste) - int(com_last.waste)
        pay_date = date.today()
        com_count = Com(electric=electric, water_h=water_h, water_c=water_c, waste=waste, date=pay_date)
        com_count.save()
        com_count.clean()

        # count data
        electric_count = int(electric) - int(com_last.electric)
        water_h_count = int(water_h) - int(com_last.water_h)
        water_c_count = int(water_c) - int(com_last.water_c)

        electric_bill = int(com_cost.electric_cost) * int(electric_count)
        water_h_bill = int(com_cost.water_h_cost) * int(water_h_count)
        water_c_bill = int(com_cost.water_c_cost) * int(water_c_count)
        waste_bill = int(com_cost.waste_cost) * int(waste_count)
        total_bill = electric_bill + water_h_bill + water_c_bill + waste_bill

        messages.success(request, 'Комуналка посчитана! ')
        messages.success(request, 'Свет: ' + str(electric_bill) + 'руб.')
        messages.success(request, 'Горячая вода: ' + str(water_h_bill) + 'руб.')
        messages.success(request, 'Холодная вода: ' + str(water_c_bill) + 'руб.')
        messages.success(request, 'Канализация: ' + str(waste_bill) + 'руб.')
        messages.success(request, 'Всего: ' + str(total_bill) + 'руб.')

    return render(request, 'count_page/count_page.html', locals())


def add_com_action(request):

    if request.method == "POST":
        print(request.POST)
        electric = request.POST['electric']
        water_h = request.POST['water_h']
        water_c = request.POST['water_c']
        pay_date = date.today()

        com_count = Com(electric=electric, water_h=water_h, water_c=water_c, date=pay_date)
        com_count.save()
        com_count.clean()
        print(request.POST)
        messages.info(request, 'Комуналка посчитана!')

        return count_page(request)


