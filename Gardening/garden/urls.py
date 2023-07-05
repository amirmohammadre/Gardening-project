from django.urls import path
from . import views



urlpatterns = [
    path('garden/', views.garden),
    path('cultivation/', views.cultivation),
    path('weeklyreport/', views.weeklyReport),
    path('api/garden/', views.GardenList.as_view()),
    path('api/garden/<int:pk>/delete/', views.GardenDelete.as_view()),
    path('api/cultivation/', views.CultivationList.as_view()),
    path('api/weeklyreport/', views.WeeklyReportList.as_view()),


]
