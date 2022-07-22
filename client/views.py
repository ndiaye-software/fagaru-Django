from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.http import HttpResponseRedirect

def load_villes(request):
    region_id = request.GET.get('region_id')
    villes = Ville.objects.filter(region_id=region_id).all()
    return render(request, 'ville_dropdown_list_options.html', {'villes': villes})

def home (request):
    return render(request,'accueil_client.html')

def RDV (request):
    return render(request,'client_rdv.html')

def contact (request):
    return render(request,'contact.html')

def consultations(request):
    return render(request,'client_consultations.html')

def profil (request):
    submitted = False
    if request.method == "POST":
        form = FirstForm(request.POST)
        form1 = SecondForm(request.POST)
        form2 = ThirdForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            form1.save()
            form2.save()
            return HttpResponseRedirect('/profil?submitted=True')
    else:
        form = FirstForm
        form1 = SecondForm
        form2 = ThirdForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "client_profil.html", {'form': form, 'form1': form1, 'form2': form2, 'submitted': submitted})

def vérification (request):
    return HttpResponse("vérification")

def paiement (request):
    return HttpResponse("paiement")

def créateur (request):
    return render(request,'créateur.html')