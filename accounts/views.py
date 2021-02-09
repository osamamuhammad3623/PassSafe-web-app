from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import registerForm
from cpg import models


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registerForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    user_passwords = models.passwords.objects.filter(id = request.user.id)
    return render(request, 'accounts/profile.html', {'user_passwords': user_passwords })

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')