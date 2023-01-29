from django import forms
from .models import annonce

class AddannonceForm(forms.ModelForm):

    class Meta:
        model = annonce
        fields = ('owner','title','module','description')
