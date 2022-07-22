from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *

def load_villes(request):
    region_id = request.GET.get('region_id')
    villes = Ville.objects.filter(region_id=region_id).all()
    return render(request, 'ville_dropdown_list_options.html', {'villes': villes})

def accueil (request):
    if request == 'POST':
        email = Email
        password1 = PasswordForm

    else:
        email = Email
        password1 = PasswordForm
    return render(request,"connexion.html", {'email' : email, 'password1' : password1,})

def patientinscription (request):
    if request.method == 'POST':
        firstname = FirstName(request.POST)
        lastname = LastName(request.POST)
        phone = Phone(request.POST)
        sexe = Sexe(request.POST)
        region = Region(request.POST)
        birthdate = Birthdate(request.POST)
        ville = Ville(request.POST)
        email = Email(request.POST)
        password1 = PasswordForm(request.POST)
        password2 = Password2Form(request.POST)
        print(request)

        if firstname.is_valid & lastname.is_valid & phone.is_valid & sexe.is_valid & region.is_valid & birthdate.is_valid & ville.is_valid & email.is_valid & password2.is_valid & password1.is_valid :
            firstname.save()
            lastname.save()
            birthdate.save()
            phone.save()
            region.save()
            ville.save()
            email.save()
            password1.save()
            password2.save()
        return redirect('/')
    else:
        firstname = FirstName
        lastname = LastName
        phone = Phone
        sexe = Sexe
        region = Region
        birthdate = Birthdate
        ville = Ville
        email = Email
        password1 = PasswordForm
        password2 = Password2Form
        print(request)
    return render(request,"inscription_client.html", {'firstname' : firstname, 'lastname' : lastname, 'phone' : phone,'sexe' : sexe, 'region' : region, 'birthdate' : birthdate, 'ville' : ville, 'email' : email, 'password1' : password1, 'password2' : password2})

