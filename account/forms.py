from re import match
import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class NameForm(forms.Form):
    id = forms.CharField(label = 'ID', max_length=12, min_length=4 )
    password = forms.CharField(label = 'PASSWORD')
    re_enter_password = forms.CharField(label = 'Re-enter PASSWORD ')
    your_name = forms.CharField(label = 'Your name', max_length=12, min_length=2)
    your_email = forms.CharField(label = 'Your E-Mail Adress')
    your_phone = forms.CharField(label= 'Your Phone Number')

  

    