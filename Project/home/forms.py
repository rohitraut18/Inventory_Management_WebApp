from django import forms
from django.contrib.auth.models import User
from home.models import Inventory 

class JoinForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('fullname', 'username', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=101)
    password = forms.CharField(widget=forms.PasswordInput())
 
class InventoryForm(forms.ModelForm):  
    class Meta:  
        model = Inventory  
        fields = "__all__"  