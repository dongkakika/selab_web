from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def people(request):
    return render(request, 'main/people.html')

def research(request):
    return render(request, 'main/research.html')

def publication(request):
    return render(request, 'main/publication.html')
