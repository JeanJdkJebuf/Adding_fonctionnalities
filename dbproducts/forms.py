# forms for dbproducts
from django import forms

class ResearchProduct(forms.Form):
    product = forms.CharField(label="product", max_length=150)
