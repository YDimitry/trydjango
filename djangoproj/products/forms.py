from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Produc Title'}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'new-class two',
                   'rows':20,
                   'cols':120}))
    class Meta:
        model = Product
        fields = ['title','description','price']
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'CFE' in title:
            return title
        else:
            raise forms.ValidationError('This is not a valid title')

class RawProductForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Produc Title'}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'new-class two',
                   'rows':20,
                   'cols':120}))
    price = forms.DecimalField()