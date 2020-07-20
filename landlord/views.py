from address.forms import AddressField
from address.models import Address
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from landlord.models import *
from django.contrib import messages

def search(request):
    form = SearchForm()
    print(request.POST.items())
    if request.method == "POST":
        search_term = SearchForm(request.POST)
        landlords = Landlord.objects.filter(address__raw__contains=search_term.data['address'])
        if landlords:
            return render(request, 'landlord/search_results.html', {'form':form,'landlords': landlords})
        else:
            messages.error(request, 'No landlord was added at this address')
            return redirect('landlord:search')
    else:
        return render(request, 'landlord/search.html', {'form':form})

def addlandlord(request):

    if request.method == 'POST':
        landlord_instance = LandlordForm(request.POST)
        #check if this landlord exists already in DB
        exists = Landlord.objects.filter(address__raw=landlord_instance.data['address']).exists()
        if exists:
            messages.error(request, 'This landlord already exists in our database')
            return redirect('landlord:add')
        else:
            landlord_instance.save()
            messages.success(request, 'Succesfully added landlord')
            return redirect('landlord:search')  # will send get request
    else:
        print("trying to add landlord")
        form = LandlordForm()
        return render(request, 'landlord/addlandlord.html', {'form': form})