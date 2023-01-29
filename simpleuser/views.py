
from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from .forms import RegistrationForm , AccountAuthenticationForm 
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    return render(request,'index.html')
def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('account:home')
        else:
            context['form'] = form


    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'account/signup.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated: 
        return redirect("account:home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print("form is valid")

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("account:home")
        else:
            print("form isnt valid")

    else:
        form = AccountAuthenticationForm()
        print("form isnt request psot")
    context['login_form'] = form