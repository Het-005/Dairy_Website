from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def bill(request):
    return HttpResponse("We are at tracker")

def profile(request):
    return HttpResponse("We are at search")

def edit(request):
    return HttpResponse("We are at product view")

def checkmilk(request):
    return HttpResponse("We are at checkout")




# Create your views here.
