from rest_framework import serializers
from .models import *


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['id', 'name', 'address', 'area', 'cultivation_pattern', 'creation_date', 'edit_date']


 
class CultivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivation
        fields = ['id', 'cultivation_date', 'piece_number']
    

 
class WeeklyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = ['id', 'report_date', 'description']









