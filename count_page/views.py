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


@login_required
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
        waste = float(water_c) - float(water_h)
        if waste < 0:
            waste = abs(waste)
        #waste_count = float(waste) - float(com_last.waste)
        pay_date = date.today()

        # count data
        electric_count = float(electric) - float(com_last.electric)
        if electric_count < 0:
            electric_count = abs(electric_count)
        water_h_count = float(water_h) - float(com_last.water_h)
        if water_h_count < 0:
            water_h_count = abs(water_h_count)
        water_c_count = float(water_c) - float(com_last.water_c)
        if water_c_count < 0:
            water_c_count = abs(water_c_count)

        electric_bill = float(com_cost.electric_cost) * float(electric_count)
        water_h_bill = float(com_cost.water_h_cost) * float(water_h_count)
        water_c_bill = float(com_cost.water_c_cost) * float(water_c_count)
        waste_bill = float(com_cost.waste_cost) * float(waste)
        internet_bill = 470
        total_com_bill = electric_bill + water_h_bill + water_c_bill + waste_bill
        total_bill = total_com_bill / 3
        total_bill_oleg = total_bill + 157
        total_bil_stasya = total_bill - 314

        com_count = Com(electric=electric, water_h=water_h, water_c=water_c, waste=waste,
                        last_bill=total_com_bill, date=pay_date)
        com_count.save()
        com_count.clean()

        messages.success(request, 'Комуналка посчитана! ')
        messages.success(request, 'Свет: ' + str(electric_bill) + 'руб.')
        messages.success(request, 'Горячая вода: ' + str(water_h_bill) + 'руб.')
        messages.success(request, 'Холодная вода: ' + str(water_c_bill) + 'руб.')
        messages.success(request, 'Канализация: ' + str(waste_bill) + 'руб.')
        messages.success(request, 'Всего комуналка: ' + str(("%.2f" % total_com_bill)) + 'руб.')
        messages.success(request, 'Олег переводит Леше: ' + str(("%.2f" % total_bill_oleg)) + 'руб.')
        messages.success(request, 'Стася переводит Леше: ' + str(("%.2f" % total_bil_stasya)) + 'руб.')

    return render(request, 'count_page/count_page.html', locals())


def index(request):

    return render(request, 'home.html', locals())






