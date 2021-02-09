from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .forms import registerForm


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registerForm()
    return render(request, 'accounts/register.html', {'title':'Register', 'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html',{'title':'Profile'} )

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')