from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout


# Create your views here.
### Provide view of Registration Page ###

def indexPage(request):
    return render(request, 'index.html')

def registerPage(request):
    form = CreateUser()
    
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
            
    
    context = {'form':form}
    return render(request, 'register.html', context)
    

### Provide view of Login Page ###


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('index')
        
    
    context= {}
    return render(request, 'login.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    