from django.contrib.auth.decorators import login_required
# main/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Change to your success URL
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    return render(request,'dashboard.html')


