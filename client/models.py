from django.db import models
from multiselectfield import MultiSelectField

class Test(models.Model) :
    test = models.CharField(max_length=30)
    def __str__ (self):
        return self.test

class Médicaux(models.Model) :
    médicaux = models.CharField(max_length=30)
    def __str__ (self):
        return self.médicaux

class Chirurgicaux(models.Model) :
    chirurgicaux = models.CharField(max_length=30)
    def __str__ (self):
        return self.chirurgicaux

class Allergies(models.Model) :

    allergies = models.CharField(max_length=30)
    def __str__ (self):
        return self.allergies

class Vaccin(models.Model) :
    Vaccin = models.CharField(max_length=30)
    def __str__ (self):
        return self.Vaccin

class Sexe(models.Model):
    Sexe = models.CharField(max_length=30)
    def __str__ (self):
        return self.Sexe

class Region(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Ville(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Client(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sexe = models.ForeignKey(Sexe, default=None, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length= 30)

    birthdate = models.DateField()
    taille = models.CharField(max_length=30)
    poids = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True,default=None)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,null=True,default=None)

    allergies = models.ForeignKey(Allergies, default=None, on_delete=models.CASCADE, null=True)
    vaccin = models.ForeignKey(Vaccin, default=None, on_delete=models.CASCADE, null=True)
    médicaux = models.ForeignKey(Médicaux, default=None, on_delete=models.CASCADE, null=True)
    chirurgicaux = models.ForeignKey(Chirurgicaux, default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.firstname+' '+self.lastname+' '+ self.email

