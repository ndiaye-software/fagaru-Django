from django.shortcuts import render
from django.http import HttpResponse

def accueil (request):
    return render(request,"connexion.html")

def patientinscription (request):
    return render(request,"inscription_client.html")

