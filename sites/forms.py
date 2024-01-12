from django import forms
from .models import Site


class AjouterSiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']

        
class ModifierSiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']
