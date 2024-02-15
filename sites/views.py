import csv
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Site
from .forms import AjouterSiteForm, ModifierSiteForm
from django.contrib import messages



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


def exporter_mots_de_passe_csv(request):
    sites = Site.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mots_de_passe.csv"'

    writer = csv.writer(response)

    writer.writerow(['Nom', 'URL', 'Identifiant', 'Mot de passe'])

    for site in sites:
        writer.writerow([site.nom, site.url, site.identifiant, site.mot_de_passe])

    return response


def importer_mots_de_passe_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Ce n\'est pas un fichier CSV.')
            return redirect('liste_sites')

        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())

        next(csv_data, None)

        for row in csv_data:
            site = Site.objects.create(
                nom=row[0],
                url=row[1],
                identifiant=row[2],
                mot_de_passe=row[3]
            )

        messages.success(request, 'Importation réussie.')
    else:
        messages.error(request, 'Erreur lors de l\'importation.')

    return redirect('liste_sites')
