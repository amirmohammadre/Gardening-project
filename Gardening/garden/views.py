from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def garden(request):
    # return HttpResponse('Hello User ...')

    all = Garden.objects.all()
    return render(request, 'garden.html', {'gardens' : all})


def cultivation(request):
    all = Cultivation.objects.all()
    return render(request, 'cultivation.html', {'cultivations' : all})


def weeklyReport(request):
    all = WeeklyReport.objects.all()
    return render(request, 'weekly_report.html', {'reports' : all})


