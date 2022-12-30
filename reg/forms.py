from dataclasses import field
import imp
from django import forms
from django.forms import ModelForm
from .models import Booking
class BookKaro(ModelForm):
    class Meta:
        model=Booking
        fields=['bookname','booknumber','bookuser','booksport','bookday','bookslot']
        labels={'bookname':'Name','booknumber':'PhoneNo','bookuser':'Booking For','booksport':'Sport','bookday':'Day','bookslot':'Slot Time'}
         