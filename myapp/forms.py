from django import forms
from myapp.models import Book, User, Orders

class bookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        