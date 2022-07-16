from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("organiser_rendezvous/", views.RDV),
    path("voir_rendezvous/", views.consultations),
    path("profil/", views.profil),
    path("contact/", views.contact),
    path("créateur/", views.créateur),
]