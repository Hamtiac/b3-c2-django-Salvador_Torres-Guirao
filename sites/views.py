from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Site
from .forms import AjouterSiteForm


class ListeSitesView(ListView):
    model = Site
    template_name = 'sites/liste_sites.html'
    context_object_name = 'sites'


class AjouterSiteView(CreateView):
    model = Site
    form_class = AjouterSiteForm
    template_name = 'sites/ajouter_site.html'
    success_url = '/sites/'  # Redirection après un ajout réussi


def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/liste_sites.html', {'sites': sites})
