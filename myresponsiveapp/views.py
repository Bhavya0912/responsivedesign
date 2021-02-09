from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'myresponsiveapp/home.html', context)

def productsresponsive(request):
    context = {}
    return render(request, 'myresponsiveapp/productsresponsive.html', context)

def peopleresponsive(request):
    context = {}
    return render(request, 'myresponsiveapp/peopleresponsive.html', context)
    
def contactus(request):
    context = {}
    return render(request, 'myresponsiveapp/contactus.html', context)



