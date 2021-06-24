from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'home': 'active'}
    return render(request, 'home.html', context)

def service(request):
    return render(request, 'service.html')

def skill(request):
    return render(request, 'skill.html')

def contact(request):
    return render(request, 'contact.html')