from .models import Site
from .forms import AjouterSiteForm, ModifierSiteForm
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/liste_sites.html', {'sites': sites})

class ListeSitesView(ListView):
    model = Site
    template_name = 'sites/liste_sites.html'
    context_object_name = 'sites'

class AjouterSiteView(CreateView):
    form_class = AjouterSiteForm
    template_name = 'sites/ajouter_site.html'
    success_url = '/sites/'
    model = Site
# Redirection après un ajout réussi

class ModifierSiteView(UpdateView):
    model = Site
    form_class = ModifierSiteForm
    template_name = 'sites/modifier_site.html'
    success_url = '/sites/'  # Redirection après une modification réussie


