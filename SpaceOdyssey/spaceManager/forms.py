from django.forms import ModelForm
from .models import Agencia

class AgenciaForm(ModelForm):
	class Meta:
		model = Agencia
		fields = '__all__'