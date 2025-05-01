# from django.contrib.auth.decorators import login_required
# # main/views.py
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .forms import CustomLoginForm

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('register')  # Change to your success URL
#     else:
#         form = CustomLoginForm()
#     return render(request, 'login.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')  # Default to dashboard if no next URL
            return redirect(next_url)
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'message': 'Hello World'})



from .forms import CustomRegistrationForm
from django.contrib.auth import login



def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # change from 'login' to 'dashboard'
    else:
        form = CustomRegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard_view(request):
    return HttpResponse("Hello World")
