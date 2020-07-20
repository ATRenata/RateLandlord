from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from addrating.models import *
from django.http import HttpResponse
from django.contrib import messages
from landlord.models import LandlordForm

def addreview(request, landlord_id):
    print("we're in addreview function")
    landlord  = Landlord.objects.get(id=landlord_id)

    if request.method == 'GET':
            form = ReviewForm()
            return render(request, 'addreview.html', {'form': form, 'landlord':landlord})
    else:
        review = Review()
        review.fixing_rate = request.POST['fixing_rate']
        review.liveable_cond = request.POST['liveable_cond']
        review.review = request.POST['review']
        review.landlord = landlord
        review.take_again = request.POST['take_again']
        review.save()
        messages.success(request, 'Thank you for your review')
        return redirect('landlord:search') # will send get request

def show_reviews(request, landlord_id):
    print("we're in show reviews function")
    landlord = Landlord.objects.get(id=landlord_id)
    reviews = Review.objects.filter(landlord_id=landlord_id)
    return render(request, 'reviews.html', {'reviews': reviews, 'landlord':landlord})