from django.shortcuts import render, redirect
from . import models


def home(request):
    return render(request, 'cpg/home.html')

def contactpage(request):
    return render(request, 'cpg/contact.html')

def contact(request):
    new_name = request.POST.get('name')
    new_email = request.POST.get('email')
    new_message = request.POST.get('message')
    new_contact = models.contact(name = new_name, email = new_email, message = new_message)
    new_contact.save()
    return redirect('home')

def store_new(request):
    if request.method == 'POST':
        new_pass = request.POST.get('password')
        hashed_pass = models.passwords.encode_pass(new_pass)
        models.passwords.objects.create(hashed_password = hashed_pass, user = request.user)
    return redirect('profile')
