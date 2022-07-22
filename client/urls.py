from django.urls import path
from . import views
app_name = 'client'
urlpatterns = [
    path("", views.home),
    path('ajax/load-villes/', views.load_villes, name='ajax_load_villes'),
    path("rendezvous/", views.RDV),
    path("profil/", views.profil),
    path("consultations/", views.consultations),
    path("vérification/", views.vérification),
    path("paiement/", views.paiement),
    path("créateur/", views.créateur),
    path("contact/", views.contact),
]