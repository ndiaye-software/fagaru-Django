from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil),
    path('inscription/', views.patientinscription),
    path('ajax/load-villes/', views.load_villes, name='ajax_load_villes'),
]