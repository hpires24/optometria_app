from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eliminar/<int:consulta_id>/', views.eliminar_consulta, name='eliminar_consulta'),
]