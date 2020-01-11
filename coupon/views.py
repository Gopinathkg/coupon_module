from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserRegistration


# Create your views here.

def index_page(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {
        'form': form
    })


def user_details(request):
    users = UserRegistration.objects.all()
    return render(request, 'user.html', {
        'users': users
    })
