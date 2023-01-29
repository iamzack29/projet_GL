from django.shortcuts import redirect, render

from module.models import matiere
from .forms import AddannonceForm
from .models import annonce

# Create your views here.
def s_annonce(request,annonce_id):
    take = annonce.objects.get(id=annonce_id)
    return render(request,'single-announcement.html',{'take':take})