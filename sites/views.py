from django.views.generic import ListView
from .models import Site


class ListeSitesView(ListView):
    model = Site
    template_name = 'sites/liste_sites.html'
    context_object_name = 'sites'
