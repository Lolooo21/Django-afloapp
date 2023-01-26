from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangoLogin
from django.contrib.auth import logout as djangoLogout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Formation

from.forms import FormationForm,LoginForm


users = [
    { "id": 1, "username": "Quentin", "role": "Admin" },
    { "id": 2, "username": "Nicolas", "role": "Surfeur" },
    { "id": 3, "username": "Samah", "role": "Maitre Pokemon" },
]

@login_required(login_url="login") # pour etre redirigé obligatoirement vers home
def home(request: HttpRequest) -> HttpResponse:
    current_user = { "name": "Quentin", "is_admin": True }
    context = { "users": users, "current_user": current_user }
    return render(request, 'afloapp/pages/home.html', context)

@login_required(login_url="login")
@permission_required(perm='afloapp.view_formation', login_url='home')
def formations(request: HttpRequest) -> HttpResponse:
    formations = Formation.objects.all().order_by("-createdAt")
    # formations = Formation.objects.filter(nom__contains="for", id__gt=2, diplomante=True)
    context = { "formations": formations }
    return render(request, 'afloapp/pages/formations.html', context)

@login_required(login_url="login")
@permission_required(perm='afloapp.view_formation', login_url='fhome')
def formation(request: HttpRequest, pk: str) -> HttpResponse:
    formation = Formation.objects.get(id=pk)
    context = { "formation": formation }
    return render(request, 'afloapp/pages/formation.html', context)

@login_required(login_url="login")
def about(request: HttpRequest, name: str) -> HttpResponse:
    context = { "email": "qa@aflokkat.com", "name": name }
    return render(request, 'afloapp/pages/about.html', context)

@login_required(login_url="login")
def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'afloapp/pages/contact.html')

@login_required(login_url="login")
@permission_required(perm='afloapp.add_formation', login_url='formation')
def create_formation(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = FormationForm(request.POST) #POST on récupère l'information 
        if form.is_valid:
            form.save()
        return redirect('formations')

    form = FormationForm()
    context = {'form': form, "type":"create"}
    return render(request, 'afloapp/pages/create_formation.html',context)

@login_required(login_url="login")
@permission_required(perm='afloapp.change_formation', login_url='formation')
def update_formation(request: HttpRequest, pk: str) -> HttpResponse:
    formation = Formation.objects.get(id=pk)
    form = FormationForm(instance=formation)
    if request.method == "POST":
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid:
            form.save()
        return redirect('formations')
    context = {'form': form,"type":"update"}
    return render(request, 'afloapp/pages/create_formation.html',context)

@login_required(login_url="login")
@permission_required(perm='afloapp.delete_formation', login_url='formation')
def delete_formation(request: HttpRequest, pk:str) -> HttpResponse:
    formation = Formation.objects.get(id=pk)
    formation.delete()
    return redirect('formations')


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username") # .get()pour récupérer un élément d'un dictionnaire python request.POST
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)#vérification de l'entree utilisateur si le username est égale à celui de la base de donnée
        except:
            messages.error(request, "Les identifiants sont incorrects")
            return redirect("login")   
        user = authenticate(request, username=username, password=password)#authentification

        if user is not None: #si touttes les informations sont corrects connection
            djangoLogin(request, user)#on récupère les informations entrées
            return redirect("home")
        else:
            messages.error(request, "Les identifiants sont incorrects")    
    return render(request, 'afloapp/pages/login.html')

def logout(request: HttpRequest) -> HttpResponse:
    djangoLogout(request)
    context = {}
    return render(request,'afloapp/pages/logout.html') 

