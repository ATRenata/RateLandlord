from django.db import models
from address.models import AddressField
from django.forms import ModelForm, TextInput, forms

class Search(models.Model):
    address = AddressField(on_delete=models.CASCADE)

class SearchForm(ModelForm):
    class Meta:
        model  = Search
        fields = ['address']

class Landlord(models.Model):
    first_name = models.CharField(help_text="First name",max_length=50)
    last_name = models.CharField(help_text="Last Name",max_length=50)
    address = AddressField(on_delete=models.CASCADE)

    def __str__(self):
        context = ""
        context += self.first_name + " "
        context += self.last_name + " "
        context += self.address.raw
        return context

class LandlordForm(ModelForm):
    class Meta:
        model = Landlord
        fields = ['first_name', 'last_name', 'address']


