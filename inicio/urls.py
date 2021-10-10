from django.urls import path

from .views import InicioListView

app_name = "inicio"

urlpatterns = [
    path('david/', InicioListView.as_view(), name="Datos")
]
