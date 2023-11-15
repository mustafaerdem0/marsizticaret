from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import login as auth_login
# Create your views here.


def login_register(request):
    return render(request,'login-register.html')



def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            User.objects.create_user(username = username, email = email, password = password)
            messages.add_message(request, messages.SUCCESS, "Hesap Oluşturuldu Giriş Yap",extra_tags="register")
            return redirect('login-register')
        else:
            messages.add_message(request, messages.WARNING, "Boş bırakma.",extra_tags="register")
    else:
        return redirect('login-register')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request,username = username,password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request, messages.WARNING, "Giriş yapıldı",extra_tags="register")
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING, "BÖLe kullanıcı yok.",extra_tags="register")
                return redirect('login-register')  
        else:
            messages.add_message(request, messages.WARNING, "Boş bırakma.",extra_tags="register")
            return redirect('login-register')
    else:
        return redirect('login-register')