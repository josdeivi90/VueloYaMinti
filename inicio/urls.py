from django.urls import path

from .views import InicioListView, InicioCreateView

app_name = "inicio"

urlpatterns = [
    path('', InicioListView.as_view(), name="Home"),
    path("create/", InicioCreateView.as_view(), name="Create")
]
