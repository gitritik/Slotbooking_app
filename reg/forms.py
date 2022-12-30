from dataclasses import field
import imp
from django import forms
from django.forms import ModelForm
from .models import Booking
class BookKaro(ModelForm):
    class Meta:
        model=Booking
        fields=('bookname','booknumber','bookuser','booksport','bookday','bookslot')
         