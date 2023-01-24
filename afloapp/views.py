from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Formation

from.forms import FormationForm


users = [
    { "id": 1, "username": "Quentin", "role": "Admin" },
    { "id": 2, "username": "Nicolas", "role": "Surfeur" },
    { "id": 3, "username": "Samah", "role": "Maitre Pokemon" },
]


def home(request: HttpRequest) -> HttpResponse:
    current_user = { "name": "Quentin", "is_admin": True }
    context = { "users": users, "current_user": current_user }
    return render(request, 'afloapp/pages/home.html', context)


def formations(request: HttpRequest) -> HttpResponse:
    formations = Formation.objects.all().order_by("-createdAt")
    # formations = Formation.objects.filter(nom__contains="for", id__gt=2, diplomante=True)
    context = { "formations": formations }
    return render(request, 'afloapp/pages/formations.html', context)


def formation(request: HttpRequest, pk: str) -> HttpResponse:
    formation = Formation.objects.get(id=pk)
    context = { "formation": formation }
    return render(request, 'afloapp/pages/formation.html', context)

def about(request: HttpRequest, name: str) -> HttpResponse:
    context = { "email": "qa@aflokkat.com", "name": name }
    return render(request, 'afloapp/pages/about.html', context)


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'afloapp/pages/contact.html')

def create_formation(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = FormationForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('formations')

    form = FormationForm()
    context = {'form': form}
    return render(request, 'afloapp/pages/create_formation.html',context)


def update_formation(request: HttpRequest, pk: str) -> HttpResponse:
    formation = Formation.objects.get(id=pk)
    form = FormationForm(instance=formation)
    if request.method == "POST":
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid:
            form.save()
        return redirect('formations')
    context = {'form': form,'formation':formation}
    return render(request, 'afloapp/pages/update_formation.html',context)

def delete_formation(request: HttpRequest, pk:str) -> HttpResponse:
    formation = Formation.objects.get(id=pk)
    formation.delete()
    return redirect('formations')