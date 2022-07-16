from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request,'accueil_client.html')

def RDV (request):
    return render(request,'client_rdv.html')

def contact (request):
    return render(request,'contact.html')

def consultations(request):
    return render(request,'client_consultations.html')

def profil (request):
    return render(request,'client_profil.html')

def vérification (request):
    return HttpResponse("vérification")

def paiement (request):
    return HttpResponse("paiement")

def créateur (request):
    return render(request,'créateur.html')