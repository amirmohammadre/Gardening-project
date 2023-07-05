from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
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






class GardenList(generics.ListCreateAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer


class GardenDelete(generics.DestroyAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer


class CultivationList(generics.ListCreateAPIView):
    queryset = Cultivation.objects.all()
    serializer_class = CultivationSerializer


class WeeklyReportList(generics.ListCreateAPIView):
    queryset = WeeklyReport.objects.all()
    serializer_class = WeeklyReportSerializer

