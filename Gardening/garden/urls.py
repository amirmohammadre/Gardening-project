from django.urls import path
from . import views



urlpatterns = [
    path('garden/', views.garden),
    path('cultivation/', views.cultivation),
    path('weeklyreport/', views.weeklyReport),

]
