from django.shortcuts import render
from django.core.validators import validate_email


def connexion(request):
    
    return render(request,'connexion.html',{})

def inscription(request):
    error = False
    message = " "
    if request.method == 'POST':
        email = request.POST.get('email', None)
        prenom = request.POST.get('prenom', None)
        nom = request.POST.get('nom', None)
        password = request.POST.get('password', None)
        conf_password = request.POST.get('conf_password', None)
        # password
        if error == False:
            if password != conf_password:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
                print('erreur')
        # Exist
        """
        verification de l'email dans la base de donner 
        user = User.objects.filter(Q(email=email))
        if user:
            error = True
            message = f"Un utilisateur avec email {email} exist déjà'!"
        """


    context = {
        'error':error,
        'message':message
    }
    return render(request,'inscription.html',{})

def home_users(request):
    return render(request,'home_users.html',{})

def deconnexion(request):
    return render(request,'connexion.html',{})
# Create your views here.
