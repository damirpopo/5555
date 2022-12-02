from django.shortcuts import render
from django.http import HttpResponse
from .forms import dostavka

def index(request):
    return render(request,"index.html")

def appointment(request):
    name = request.POST.get("name", "noname")
    email = request.POST.get("email", "noemail")
    number = request.POST.get("number", "nonumber")
    service = request.POST.get("service", "noserves")
    text = request.POST.get("dad", "notext")
    return HttpResponse(f"<h2>Name: {name} email: {email} number: {number} service:{service} <br> text: {text}")

def dost(request):
    if request.method == "POST":
        name = request.POST.get("name", "noname")
        fam = request.POST.get("fam", "nofam")
        mail = request.POST.get("mail", "nomail")
        adres = request.POST.get("adres", "noserves")
        return HttpResponse(f"<h2>{name} {fam} mail: {mail} adres: <br>{adres} ")
    else:
        form = dostavka()
        return render(request, "dost.html", {"form": form})
