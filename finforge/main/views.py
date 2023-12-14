from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from main.models import Client


# def login_page(request):

#     if request.method == "POST":
#         username = request.POST.get('username'),
#         password = request.POST.get('password'),
    
#     user = authenticate(username = username, password = password)

#     if user is None:
#         messages.error(request, 'Invalid password')
#         return(redirect, '/login/')
    
#     else:
#         login(user)
#         # return render(redirect, "login.html")
    
#     # if User.objects.filter(username = username).exists():
#         return render(request, 'login.html')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # email = request.POST.get('email')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
# not User.objects.filter(username=username).exists() or

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/mainpage/')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            # last_name = last_name,
            username = username,
            # password = password
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')

        return redirect('/register/')
    
    return render(request, 'register.html')


# def register(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # islawyer = request.POST.get('islawyer')

#         user = User.objects.filter(username=username)
#         if user.exists():
#             messages.info(request, "Username already exists.")
#             return redirect('/register/')

#         user=User.objects.create(
#             first_name = first_name,
#             last_name = last_name,
#             username = username,
#         )

#         user.set_password(password)
#         user.save()

#         # if islawyer is "True":
#         #     islawyer = bool(True)
#         # else:
#         #     islawyer = bool(False)

#         client = Client.objects.create(
#             user = user,
#         )

#         client.save()

#         messages.info(request, "Account created successfully.")
#         return render(request, 'register.html')


# Create your views here.


def mainpage(request):
    return render(request, "gg.html")