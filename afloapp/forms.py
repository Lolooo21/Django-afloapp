from django.forms import ModelForm
from.models import Formation

from django.contrib.auth.models  import User

#création de formulaire!!

class FormationForm(ModelForm):# ModelForm paramètre par défaut de Django
    class Meta:
        model = Formation
        fields = '__all__' # ['nom','description]
        exclude = ['diplomante']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']        