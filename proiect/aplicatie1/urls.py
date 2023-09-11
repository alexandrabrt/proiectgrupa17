from django.urls import path
from aplicatie1 import views

app_name = 'aplicatie1'

urlpatterns = [
    path('adaugare/', views.CreateLocationView.as_view(), name='adaugare'),
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('<int:pk>/modificare/', views.UpdateLocationView.as_view(), name='modifica'),
    path('<int:pk>/sterge/', views.delete_location, name='sterge'),
    path('<int:pk>/dezactiveaza/', views.deactivate_location, name='dezactiveaza'),
    path('<int:pk>/activeaza/', views.activate_location, name='activeaza'),

    path('start_timesheet/', views.new_timesheet, name='start_pontaj'),
    path('end_timesheet/', views.stop_timesheet, name='end_pontaj'),
]
