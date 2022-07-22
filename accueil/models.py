from django.db import models

class Sexe(models.Model) :
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

class UserModel(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    sexe = models.ForeignKey(Sexe, default=None, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length= 30)
    password = models.CharField(max_length=30, null=True)
    password2 = models.CharField(max_length=30, null=True)
    birthdate = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default=None)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, null=True, default=None)


