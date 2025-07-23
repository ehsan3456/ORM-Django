from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages as message
from django.shortcuts import redirect
# Create your views here.
def home(request):
        if request.method == 'POST':
            username  = request.POST['username']
            password =  request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                message.success(request, 'You have successfully logged in')
                return redirect('home')
            else:
                message.success(request, 'There was an error logging in, please try again')
                return redirect('home')
        else:
            return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
        logout(request)
        message.success(request, 'You have successfully logged out')    
        return redirect('home')