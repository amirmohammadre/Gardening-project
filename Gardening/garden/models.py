from django.db import models


class Garden(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField()
    area = models.PositiveIntegerField()
    cultivation_pattern = models.CharField(max_length = 50)
    creation_date = models.DateField()
    edit_date = models.DateField()



class Cultivation(models.Model):
    garden = models.ForeignKey(Garden, on_delete = models.CASCADE)
    cultivation_date = models.DateField()
    piece_number = models.PositiveIntegerField()



class WeeklyReport(models.Model):
    garden = models.ForeignKey(Garden, on_delete = models.CASCADE) 
    report_date = models.DateField()
    description = models.TextField()

