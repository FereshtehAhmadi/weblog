from django.shortcuts import render, redirect
from app.models import Post
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'app/login.html')
    else:
        user_form = UserRegistrationForm()
        return render(request,'app/register.html',{'user_form': user_form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username =username, password= password)
        if user is not None:
            obj = User.objects.get(username= username)
            return redirect('home', {'user': obj.username})
    return render(request, 'app/login.html')


def home(request, user):
    obj = User.objects.get(username= user)
    content = {
        'user': obj.username ,
        'posts': Post.objects.all(),
    }
    return render(request, 'app/home.html', content)


def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        p = Post(title=title, content=content)
        p.save()
        return redirect('home')
    return render(request, 'app/add.html')

