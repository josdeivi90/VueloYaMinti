
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='Home'),
    path('inicio/',include('inicio.urls', namespace='inicio'))
]
