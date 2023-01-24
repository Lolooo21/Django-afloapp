from django.forms import ModelForm
from.models import Formation


class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = '__all__' # ['nom','description]
        exclude = ['diplomante']