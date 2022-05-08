from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
        widgets = {
        'username' : forms.TextInput(attrs={'class': 'form-control'}),
        'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
        'last_name' : forms.TextInput(attrs={'class': 'form-control' ,}),
        'email' : forms.TextInput(attrs={'class': 'form-control col-12', 'style': 'width: 100%'}),
    }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    


# def register(request):
#     register_Form = User(request.POST)
#     if register_Form.is_valid():
#         username = register_Form.clean_data.get('username')
#         password = register_Form.clean_data.get('password')
#         fname = register_Form.clean_data.get('firstName')
#         lname = register_Form.clean_data.get('lastName')
#         email = register_Form.clean_data.get('email')
        
#         user: bool = User.objects.filter(username= username).exist()
#         if user:
#             register_Form.add_error('username', 'doplicate username!!')
#         else:
#             new_user = User(username= username, firstName= fname, lastName= lname, email= email)
#             new_user.set_password(password)
#             new_user.save()
#         return redirect('login')
    
#     return render(request, 'app/register.html')
