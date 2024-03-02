from django.urls import path
from users.views import (
    connexion, inscription, home_users, deconnexion,
)
urlpatterns = [
    path('', home_users, name='home_users'),
    path('connexion', connexion, name='connexion'),
    path('inscription', inscription, name='inscription'),
    path('deconnexion', deconnexion, name='deconnexion'),
]
