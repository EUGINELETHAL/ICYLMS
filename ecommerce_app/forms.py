from django import forms
from .models import Order
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, Select
from django.contrib.auth.models import User
from account.models import PrivateMessage,Student

class CartForm(forms.Form):
    quantity = forms.Field(initial=1 , disabled=True, widget=forms.HiddenInput)
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CartForm, self).__init__(*args, **kwargs)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('paid',)
        fields = { 'name', 'email'}
        labels = {
           'email' :'email :',
           'name' : 'name :'

          
        }

        widgets = {
            # 'address': forms.Textarea(attrs={'row': 5, 'col': 8}),

            'name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your name here'}),
            'email': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your email here'}),



        }
