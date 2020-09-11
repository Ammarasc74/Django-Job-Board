from django import forms

from .models import apply , job



class applyform(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name','email','website','cv','cover_letter']



class jobform(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner','slug',)