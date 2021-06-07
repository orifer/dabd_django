# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
# https://docs.djangoproject.com/en/3.2/ref/forms/widgets/

from functools import partial
from django import forms
from django.forms import ModelForm
from .models import Agencia, Missio, Nau

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