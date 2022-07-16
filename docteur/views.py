from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request,'accueil_docteur.html')

def RDV (request):
    return render(request,'accueil_docteur.html')

def contact (request):
    return HttpResponse("contact")

def consultations(request):
    return HttpResponse("consultations")

def créateur (request):
    return render(request,'créateur.html')

def profil (request):
    return HttpResponse("profil")