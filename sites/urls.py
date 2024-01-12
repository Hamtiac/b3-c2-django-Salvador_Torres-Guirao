from django.urls import path
from .views import ListeSitesView
from .views import ListeSitesView, AjouterSiteView


urlpatterns = [
    path('sites/', ListeSitesView.as_view(), name='liste_sites'),
    path('ajouter_site/', AjouterSiteView.as_view(), name='ajouter_site'),
    path('modifier_site/<int:pk>/', ModifierSiteView.as_view(), name='modifier_site'),
]
