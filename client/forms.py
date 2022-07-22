from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm
from .models import *
from django import forms

class FirstForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super(FirstForm, self).__init__(*args, **kwargs)
		self.fields['birthdate'].empty_label = 'Précisez votre région'

	class Meta :
		model = Client
		fields = ['firstname','lastname','birthdate','email','phone']

		labels = {
			'lastname': '',
			'firstname': '',
			'birthdate': '',
			'email': '',
			'phone': '',
		}
		widgets ={
			'firstname': forms.TextInput(attrs={'placeholder': 'Entrez votre prénom'}),
			'lastname': forms.TextInput(attrs={'placeholder': 'Entrez votre nom'}),
			'birthdate': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
			'email': forms.TextInput(attrs={'placeholder': 'Entrez votre mail'}),
			'phone': forms.TextInput(attrs={'placeholder': 'Enter votre numéro'}),
		}

class SecondForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(SecondForm, self).__init__(*args, **kwargs)

		self.fields['region'].empty_label = 'Précisez votre région'
		self.fields['ville'].empty_label = 'Précisez votre ville'
		self.fields['sexe'].empty_label = 'Précisez votre sexe'


		if 'region' in self.data:
			try:
				region_id = int(self.data.get('region'))
				self.fields['ville'].queryset = Region.objects.filter(region_id=region_id).order_by('name')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['ville'].queryset = self.instance.region.ville_set.order_by('name')

	class Meta :
		model = Client
		fields =  ['taille','poids','sexe','region','ville']
		labels = {
			'taille': '',
			'poids': '',
			'sexe': '',
			'region': '',
			'ville': '',
		}
		widgets = {
			'taille': forms.TextInput(attrs={'placeholder': 'Entrez votre taille en cm'}),
			'poids': forms.TextInput(attrs={'placeholder': 'Entrez votre poids en kg'}),
			'sexe': forms.Select(),
			'region': forms.Select(),
			'ville': forms.Select(),
		}

class ThirdForm(ModelForm):


	def __init__(self, *args, **kwargs):

		super(ThirdForm, self).__init__(*args, **kwargs)
		self.fields['médicaux'].empty_label = "Antécédents médicaux"
		self.fields['chirurgicaux'].empty_label = 'Antécédents chirurgicaux'
		self.fields['allergies'].empty_label = 'Vos allergies'
		self.fields['vaccin'].empty_label = 'Vos vaccins'

	class Meta :

		model = Client

		fields = ['médicaux','chirurgicaux','allergies','vaccin']
		labels = {
			'médicaux': '',
			'chirurgicaux': '',
			'allergies': '',
			'vaccin': '',
		}





