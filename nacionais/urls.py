"""
URL configuration for sinopse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
app_name = 'nac'
urlpatterns = [
    path('', views.v_nacionais, name='pg_inicial'),
    path('acao/', views.v_nac_acao, name='acao'),
    path('comedia/', views.v_nac_comedia, name='comedia'),
    path('documentario/', views.v_nac_documentario, name='documentario'),
    path('drama/', views.v_nac_drama, name='drama'),
    path('terror/', views.v_nac_terror, name='terror'),
    path('<str:genero>/<str:titulo>', views.v_nac_detalhamento , name='detalhes')
    
]
