from django.urls import path
from .views import ListeSitesView

urlpatterns = [
    path('sites/', ListeSitesView.as_view(), name='liste_sites'),
]
