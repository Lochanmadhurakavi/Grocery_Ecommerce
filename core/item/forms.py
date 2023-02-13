from django import forms

from item.models import Item, Category

class AddNewItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Select category'
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Item name'
            }),

            
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Item description'
            }),

            
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Item price'
            }),

            
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Item image'
            }),
        }


class AddNewCategories(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'image',)

        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name of the categpry'
            }),

            'image':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'Add image'
            }),


        }