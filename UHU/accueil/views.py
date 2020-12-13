from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, 'pages/accueil.html')

def propos(request):
    return render(request, 'pages/propos.html')

