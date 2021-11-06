from django import forms
from products.models import Product, Category


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'price',
                  'description', 'category')
        widgets = {
            'name': forms.TextInput(attrs=\
                {'class': 'form-control',
                 'placeholder': 'Name'}),
            'price': forms.TextInput(attrs= \
                {'class': 'form-control',
                 'placeholder': 'Price'}),
            'description': forms.Textarea(attrs=\
                {'class': 'form-control',
                 'placeholder': 'Description'}),
            'category': forms.Select(attrs=\
                {'class': 'custom-select',
                 'placeholder': 'Category'}),
            'seller': forms.Select(attrs=\
                {'class': 'custom-select',
                 'placeholder': 'Seller'}),
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs=\
                {'class': 'form-control',
                 'placeholder': 'Category Name'}),
        }