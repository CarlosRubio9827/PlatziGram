"""User views."""

# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username," ", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('feed')
        else:

            return render(request, 'users/login.html')
