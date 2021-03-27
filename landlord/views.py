from address.forms import AddressField
from address.models import Address
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from addrating.models import Review
from landlord.models import *
from django.contrib import messages



def search(request):
    form = SearchForm()
    print(request.POST.items())
    if request.method == "POST":
        search_term = SearchForm(request.POST)
        landlords = Landlord.objects.filter(address__raw__contains=search_term.data['address'])
        if len(landlords) != 0:
            return render(request, 'landlord/search_results.html', {'form':form,'landlords': landlords})
        else:
            messages.add_message(request, messages.WARNING, 'No landlord was added at this address. You can click on Add Landlord to add one.')
            return redirect('landlord:search')
    else:
        landlords = Landlord.objects.all()
        l = len(landlords)
        landlords = landlords[(l-3):]
        list = []
        for x in range(len(landlords)):
            r = Review.objects.filter(landlord_id=landlords[x].id)[0].review
            list.append(r)

        return render(request, 'landlord/search.html', {'form':form, 'landlords':landlords, 'list':list})

def addlandlord(request):

    if request.method == 'POST':
        landlord_instance = LandlordForm(request.POST)
        exists = Landlord.objects.filter(address__raw=landlord_instance.data['address']).exists()
        if exists:
            messages.error(request, 'This landlord already exists in our database')
            return redirect('landlord:add')
        else:
            landlord_instance.save()
            id   = Landlord.objects.filter(address__raw=landlord_instance.data['address']).values('id')[0]['id']
            messages.success(request, 'Succesfully added landlord')
            return redirect('addrating:review', landlord_id=id)  # will send get request
    else:
        print("trying to add landlord")
        form = LandlordForm()
        return render(request, 'landlord/addlandlord.html', {'form': form})