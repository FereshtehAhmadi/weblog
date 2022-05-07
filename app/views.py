from django.shortcuts import render, redirect
from app.models import Person, Post
from .forms import UserRegistrationForm


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
    return render(request, 'app/login.html')
    


# def login(request):
#     if request.method == 'POST':
#         userName = request.POST['username']
#         password = request.POST['password']
#         if Person.objects.filter(userName=userName).exists() == True:
#             obj = Person.objects.get(userName=userName)
#             if obj.password == password:
#                 userName = request.session[obj.userName]
#                 user = request.session[obj.id]
#                 return redirect('home')
#     return render(request, 'app/login.html')


# def register(request):
#     if request.method == 'POST':
#         userName = request.POST['username']
#         firstName = request.POST['fname']
#         lastName = request.POST['lname']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         p = Person(userName=userName, firstName=firstName, lastName=lastName, password=password, email=email)
#         p.save()
#         return redirect('login')
    
#     return render(request, 'app/register.html')



# def home(request):
#     content = {
#         'posts': Post.objects.all(),
#     }
#     return render(request, 'app/home.html', content)


# def add_post(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         p = Post(title=title, content=content)
#         p.save()
#         return redirect('home')
#     return render(request, 'app/add.html')

