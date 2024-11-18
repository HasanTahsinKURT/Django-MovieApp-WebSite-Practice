from django.shortcuts import render
from .models import Category,Movie


kategori_liste = ["macera","korku","komedi","bilim kurgu"]
film_liste = [
    {
    "id":1, 
    "film_adi":"Uncharted",
    "aciklama":"Uncharted, Hazine Avi",
    "resim"   :"uncharted.jpg",  
    "anasayfa":True,
    },
    {
    "id":2, 
    "film_adi":"Terrifier",
    "aciklama":"Terrifier, Hallowen Katili",
    "resim"   :"terrifier.jpg",
    "anasayfa":True,
    },
    {
    "id":3, 
    "film_adi":"Dictator",
    "aciklama":"Dictator, Amerikan Komedi",
    "resim"   :"dictator.jpg",    
    "anasayfa":False,
    },
    {
    "id":4, 
    "film_adi":"İnterstellar",
    "aciklama":"İnterstellar, Yıldızlararası Yolculuk",
    "resim"   :"interstellar.jpg",
    "anasayfa":True,
    },
]

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler" : Movie.objects.filter(anasayfa = True),
    }
    return render(request,"home.html",data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler" : Movie.objects.all(),
    }
    return render(request,"movies.html",data)

def moviedetails(request,id):
    data = {
        "movie" : Movie.objects.get(id = id)
    }
    return render(request,"details.html",data)