
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm


from django.contrib.auth.forms import UserCreationForm
User=get_user_model()

# Create your views here.

# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')

#         user1 = User.objects.create_user(username,email,pass1)
#         user1.first_name = fname
#         user1.last_name = lname

#         user1.save()

#         messages.success(request, "account created successfully")

#         return redirect('signin')
#     return render(request,"authentication/signup.html")





        




# def signin(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         pass1 = request.POST.get('pass1')

#         user = authenticate(username=username, password = pass1)

#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             return render(request, "authentication/index.html", {'fname': fname})
        
#             try:
#                 user = User.objects.create_user(username, email, password)
#     # ... (rest of the user creation code)
#             except IntegrityError:
#              messages.error(request, "Username already exists. Please choose a different username.")

#     return render(request, "authentication/signin.html")

# def signout(request):
#    pass


from django.contrib.auth.hashers import make_password



from django.shortcuts import render, redirect
from .forms import UserRegistrationForm



def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            # login(request, user) 
            return redirect('login_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/signup.html', {'form': form})


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['uname']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            elif user.is_staff:
                request.session['uname'] = username
                return redirect('home')
            else:
                return redirect('home')
        else:
            return render(request, 'authentication/signin.html', {'form': form, 'login_failed': True})

    return render(request, 'authentication/signin.html', {'form': form})
def logout_user(request):
    logout(request)
    return redirect('home')