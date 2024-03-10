# myapp/forms.py
from django import forms
from .models import Car

class CarForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    car_model = forms.ModelChoiceField(queryset=Car.objects.all())
    comments = forms.CharField(widget=forms.Textarea, required=False)
