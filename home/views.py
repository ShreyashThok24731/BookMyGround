from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# render -> to render the templates

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        Email = request.POST.get('Email')
        Mobile = request.POST.get('Mobile')
        Desc = request.POST.get('Desc')
        contact = Contact(Firstname=Firstname, Lastname=Lastname,
                          Mobile=Mobile, Desc=Desc, Email=Email, Date=datetime.today())
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request, 'contact.html')


def payment(request):
    if request.method == 'POST':
        print("Hello World")
        name = request.POST.get('name')
        ground = request.POST.get('ground')
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')
        print(name, ground, date, time_slot)

        # Save the data to the database
        booking = Booking(name=name, ground=ground,
                          date=date, time_slot=time_slot)
        booking.save()
        print(request)
    return render(request, 'payment.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        Password = request.POST.get('Password')
        user = authenticate(request, username=username, password=Password)
        if user is not None:

            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!")
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        uname = request.POST.get('Username')
        email = request.POST.get('Email')
        pass1 = request.POST.get('Password1')
        pass2 = request.POST.get('Password2')
        if (pass1 != pass2):
            return HttpResponse("Your Password and Confirm Password are not same!")
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')


def pune(request):
    return render(request, 'pune.html')


def pune1(request):
    return render(request, 'pune1.html')


def payment(request):
    return render(request, 'payment.html')


def book(request):
    return render(request, 'book.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
