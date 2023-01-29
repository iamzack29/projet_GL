
from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
import announecements
from announecements.models import annonce

from module.models import matiere
from .forms import RegistrationForm , AccountAuthenticationForm 
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    if not request.user.is_authenticated: 
        return redirect("simpleuser:signin")
    Owner = request.user
    list = matiere.objects.all()
    list2 = annonce.objects.all()
    print(list)
    if request.POST:
        title = request.POST.get("title")
        print(title)
        description = request.POST.get("description")
        print(description)
        print(Owner,title,description)
        print(request.POST.get("module"))
        if title and description:
            module = matiere.objects.get(nom=request.POST.get("module"))
            req = annonce.objects.create(owner=Owner,module=module,title=title ,description=description )
            req.save
            return redirect("simpleuser:home")
        else:
            print("error")
    
    return render(request,'index.html',{'list':list,'list2':list2})

def logout_view(request):
    logout(request)
    return redirect('simpleuser:signin')

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
            return redirect('simpleuser:home')
        else:
            context['form'] = form


    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'signup.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated: 
        return redirect("simpleuser:home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print("form is valid")

            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("simpleuser:home")
        else:
            print("form isnt valid")

    else:
        form = AccountAuthenticationForm()
        print("form isnt request psot")
    context['login_form'] = form

    # print(form)
    return render(request, "login.html", context)



def profile_view(request):
    return render(request, "profile.html")