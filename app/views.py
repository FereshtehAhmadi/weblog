from django.shortcuts import render, redirect
from app.models import Person

def home(request):
    return render(request, 'app/home.html')


def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        if Person.objects.filter(userName=userName).exists() == True:
            obj = Person.objects.get(userName=userName)
            if obj.password == password:
                return redirect('home')
    return render(request, 'app/login.html')


def register(request):
    if request.method == 'POST':
        userName = request.POST['username']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        
        p = Person(userName=userName, firstName=firstName, lastName=lastName, password=password, email=email)
        p.save()
        return redirect('login')
    
    return render(request, 'app/register.html')