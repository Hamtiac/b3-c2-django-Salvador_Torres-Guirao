from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Site
from .forms import AjouterSiteForm, ModifierSiteForm



def liste_sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/liste_sites.html', {'sites': sites})


class ListeSitesView(ListView):
    model = Site
    template_name = 'sites/liste_sites.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.filter(user=self.request.user)


class AjouterSiteView(CreateView):
    form_class = AjouterSiteForm
    template_name = 'sites/ajouter_site.html'
    success_url = '/sites/'
    model = Site
# Redirection après un ajout réussi

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ModifierSiteView(UpdateView):
    model = Site
    form_class = ModifierSiteForm
    template_name = 'sites/modifier_site.html'
    success_url = '/sites/'  # Redirection après une modification réussie


class SupprimerSiteView(DeleteView):
    model = Site
    template_name = 'sites/supprimer_site.html'
    success_url = reverse_lazy('liste_sites')
