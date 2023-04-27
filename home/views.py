from django.shortcuts import render, HttpResponse
# render -> to render the templates 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def book(request):
    return render(request, 'book.html')





