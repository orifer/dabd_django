# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
# https://docs.djangoproject.com/en/3.2/ref/forms/widgets/

from django.forms import ModelForm
from .models import Agencia

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