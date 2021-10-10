from django.urls import path

from .views import InicioListView

app_name = "inicio"

urlpatterns = [
    path('', InicioListView.as_view(), name="Home")
]
