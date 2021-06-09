# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
# https://docs.djangoproject.com/en/3.2/ref/forms/widgets/

from functools import partial
from django import forms
from django.forms import ModelForm
from .models import Agencia, Missio, Nau, Plataforma, Astronauta, Llancament

''' AGENCIES '''

class AgenciaForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['nom'].label = 'Nom'

	class Meta:
		model = Agencia
		fields = ['nom']

class AgenciaFormLectura(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['nom'].widget.attrs['readonly'] = 'readonly'
		self.fields['nom'].label = 'Nom'

	class Meta:
		model = Agencia
		fields = ['nom']



''' MISSIONS '''

class MissioForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['descripcio'].widget.attrs['class'] = 'form-control'
		self.fields['data_finalitzacio'].widget.attrs['class'] = 'form-control datepicker'
		self.fields['agencia'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Missio
		fields = ['nom', 'descripcio', 'data_finalitzacio', 'agencia']

class MissioFormLectura(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['nom'].widget.attrs['readonly'] = 'readonly'

		self.fields['descripcio'].widget.attrs['class'] = 'form-control'
		self.fields['descripcio'].widget.attrs['readonly'] = 'readonly'

		self.fields['data_finalitzacio'].widget.attrs['class'] = 'form-control datepicker'
		self.fields['data_finalitzacio'].widget.attrs['readonly'] = 'readonly'

		self.fields['agencia'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['readonly'] = 'readonly'

	class Meta:
		model = Missio
		fields = ['nom', 'descripcio', 'data_finalitzacio', 'agencia']



''' NAUS '''

class NauForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['capacitat'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Nau
		fields = ['nom', 'capacitat', 'agencia']

class NauFormLectura(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['nom'].widget.attrs['readonly'] = 'readonly'

		self.fields['capacitat'].widget.attrs['class'] = 'form-control'
		self.fields['capacitat'].widget.attrs['readonly'] = 'readonly'

		self.fields['agencia'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['readonly'] = 'readonly'

	class Meta:
		model = Nau
		fields = ['nom', 'capacitat', 'agencia']



''' PLATAFORMA '''

class PlataformaForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['latitud'].widget.attrs['class'] = 'form-control'
		self.fields['longitud'].widget.attrs['class'] = 'form-control'
		self.fields['pais'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Plataforma
		fields = ['nom', 'latitud', 'longitud', 'pais', 'agencia']

class PlataformaFormLectura(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['nom'].widget.attrs['readonly'] = 'readonly'

		self.fields['latitud'].widget.attrs['class'] = 'form-control'
		self.fields['latitud'].widget.attrs['readonly'] = 'readonly'

		self.fields['longitud'].widget.attrs['class'] = 'form-control'
		self.fields['longitud'].widget.attrs['readonly'] = 'readonly'

		self.fields['pais'].widget.attrs['class'] = 'form-control'
		self.fields['pais'].widget.attrs['readonly'] = 'readonly'

		self.fields['agencia'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['readonly'] = 'readonly'

	class Meta:
		model = Plataforma
		fields = ['nom', 'latitud', 'longitud', 'pais', 'agencia']




''' ASTRONAUTES '''


class AstronautaForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['cognom'].widget.attrs['class'] = 'form-control'
		self.fields['naixement'].widget.attrs['class'] = 'form-control datepicker'
		self.fields['genere'].widget.attrs['class'] = 'form-control'
		self.fields['altura'].widget.attrs['class'] = 'form-control'
		self.fields['grup_sanguini'].widget.attrs['class'] = 'form-control'
		self.fields['pais'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = Astronauta
		fields = ['nom', 'cognom', 'naixement', 'genere', 'altura', 'grup_sanguini', 'pais', 'agencia']

class AstronautaFormLectura(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nom'].widget.attrs['class'] = 'form-control'
		self.fields['nom'].widget.attrs['readonly'] = 'readonly'

		self.fields['cognom'].widget.attrs['class'] = 'form-control'
		self.fields['cognom'].widget.attrs['readonly'] = 'readonly'

		self.fields['naixement'].widget.attrs['class'] = 'form-control'
		self.fields['naixement'].widget.attrs['readonly'] = 'readonly'

		self.fields['genere'].widget.attrs['class'] = 'form-control'
		self.fields['genere'].widget.attrs['readonly'] = 'readonly'

		self.fields['altura'].widget.attrs['class'] = 'form-control'
		self.fields['altura'].widget.attrs['readonly'] = 'readonly'

		self.fields['grup_sanguini'].widget.attrs['class'] = 'form-control'
		self.fields['grup_sanguini'].widget.attrs['readonly'] = 'readonly'

		self.fields['pais'].widget.attrs['class'] = 'form-control'
		self.fields['pais'].widget.attrs['readonly'] = 'readonly'

		self.fields['agencia'].widget.attrs['class'] = 'form-control'
		self.fields['agencia'].widget.attrs['readonly'] = 'readonly'

	class Meta:
		model = Astronauta
		fields = ['nom', 'cognom', 'naixement', 'genere', 'altura', 'grup_sanguini', 'pais', 'agencia']



''' LLANÇAMENTS '''


class LlancamentForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['missio'].widget.attrs['class'] = 'form-control'
		self.fields['nau'].widget.attrs['class'] = 'form-control'
		self.fields['plataforma'].widget.attrs['class'] = 'form-control'
		self.fields['data_llancament'].widget.attrs['class'] = 'form-control datepicker'

	class Meta:
		model = Llancament
		fields = ['missio', 'nau', 'plataforma', 'data_llancament']

class LlancamentFormLectura(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['missio'].widget.attrs['class'] = 'form-control'
		self.fields['missio'].widget.attrs['readonly'] = 'readonly'

		self.fields['nau'].widget.attrs['class'] = 'form-control'
		self.fields['nau'].widget.attrs['readonly'] = 'readonly'

		self.fields['plataforma'].widget.attrs['class'] = 'form-control'
		self.fields['plataforma'].widget.attrs['readonly'] = 'readonly'

		self.fields['data_llancament'].widget.attrs['class'] = 'form-control'
		self.fields['data_llancament'].widget.attrs['readonly'] = 'readonly'

	class Meta:
		model = Llancament
		fields = ['missio', 'nau', 'plataforma', 'data_llancament']

