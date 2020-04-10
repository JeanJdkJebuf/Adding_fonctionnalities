from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm, ConnexionForm, CustomUserChangeForm, CustomUserChangePassword

def create_user(request):
    """ This function will be used to display a template for user creation"""
    DICTIO = {
        "create_title":"Création de compte",
                "create_user_temp":{
                    "welc_title":"Bienvenue sur la page d'inscription",
                    "temp_one":"Veuillez remplir ce formulaire pour vous inscrire",
                    "confirm":"Confirmer",
                    "already_logged_in":"Vous êtes déjà connecté en tant \
qu'utilisateur, vous ne pouvez pas créer un autre compte pour le moment.",
                }
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            messages.success(request, "Votre Compte est maintenant créé")
            return redirect('homepage')
        else:
            DICTIO["form"] = form

    else:
        form = CustomUserCreationForm()
        DICTIO["form"] = form
    return render(request, "users/create_user.html",
                  DICTIO,
                 )

def log_in(request):
    """ This function will display a template for user identification"""
    DICTIO = {
        "log_title":"Connexion",
        "text_create_acc":"Pas de compte ? Vous pouvez en créer un !",
        "create_acc":"Inscription",
        "log_in_temp":{
            "welc_title":"Se connecter",
            "err_connexion":"Utilisateur inconnu ou mauvais mot de passe",
            "button_connect":"Connexion",
        },"redirect_url" : request.GET.get('next', "homepage"),
    }

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(DICTIO["redirect_url"])
            else:
                messages.error(request, " Utilisateur ou mot de passe incorrect")

    else:
        form = ConnexionForm()
    DICTIO["form"] = form

    return render(request, 'users/login.html', DICTIO)

def disconnect_user(request):
    if request.user.is_authenticated:
        messages.success(request, "Vous êtes déconnecté")
        logout(request)
    return redirect("homepage")

@login_required(login_url='/users/log_in/')
def user_informations(request):
    DICTIO = {
        "consult_title":"Mon profil",
        "title_profile":"Profil de l'utilisateur",
        "username":"Identifiant",
        "info_user":"Profil de l'utilisateur",
        "name":"Adresse mail",
        "modify":"Modifier mes informations",
    }
    DICTIO["user"] = request.user
    return render(request,
                  "users/user_informations.html",
                  DICTIO,
                 )

@login_required(login_url='/users/log_in/')
def edit_profile(request):
    """ This function will display a template for user deletion"""
    DICTIO = {
        "change_info_temp":{
            "welc_title": "Informations du compte",
            "modif_one":"Vous pouvez changer les informations ci-dessous",
            "apply_advert":"Pour appliquer les changements, veuillez appuyer sur \
sur le bouton ci-dessous",
            "passw":"changer password",
            "confirm":"confirmer",
        }
    }

    if "passw" in request.POST:
        return redirect("change_password")

    if request.method == "POST" and "confirm" in request.POST:
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Le profil a été mis à jour")
            return redirect("edit_profile")
    else:
        form = CustomUserChangeForm(instance=request.user)
        DICTIO["form"] = form
    return render(request,
                  "users/edit_profile.html",
                  DICTIO,
                 )

@login_required(login_url='/users/log_in/')
def change_password(request):
    """ changing user's password"""
    DICTIO = {
        "change_passw":{
            "change_pass_title":"Changement de mot de passe",
            "confirm_pass":"Confirmer",
        }
    }

    if request.method == "POST":
        form = CustomUserChangePassword(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Votre mot de passe est mis à jour")
            return redirect("change_password")
        else:
            DICTIO["form"] = form

    else:
        form = CustomUserChangePassword(request.user)
        DICTIO["form"] = form
    return render(request,
                  'users/change_password.html',
                  DICTIO,
                  )
