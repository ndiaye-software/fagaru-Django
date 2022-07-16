from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("rendezvous/", views.RDV),
    path("profil/", views.profil),
    path("consultations/", views.consultations),
    path("vérification/", views.vérification),
    path("paiement/", views.paiement),
    path("créateur/", views.créateur),
    path("contact/", views.contact),
]