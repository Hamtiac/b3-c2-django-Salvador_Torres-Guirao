from django.urls import path
from .views import ListeSitesView, AjouterSiteView, ModifierSiteView, SupprimerSiteView, exporter_mots_de_passe_csv

urlpatterns = [
    path('sites/', ListeSitesView.as_view(), name='liste_sites'),
    path('ajouter_site/', AjouterSiteView.as_view(), name='ajouter_site'),
    path('modifier_site/<int:pk>/', ModifierSiteView.as_view(), name='modifier_site'),
    path('supprimer_site/<int:pk>/', SupprimerSiteView.as_view(), name='supprimer_site'),
    path('exporter-mots-de-passe/', exporter_mots_de_passe_csv, name='exporter_mots_de_passe_csv'),
]
