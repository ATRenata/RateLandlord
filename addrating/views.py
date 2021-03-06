from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from addrating.models import *
from django.http import HttpResponse
from django.contrib import messages
from landlord.models import LandlordForm
from django.db.models import Avg

def addreview(request, landlord_id):
    print("we're in addreview function")
    landlord = Landlord.objects.get(id=landlord_id)

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
        return show_reviews(request, landlord_id)

def show_reviews(request, landlord_id, ):
    print("we're in show reviews function")
    landlord = Landlord.objects.get(id=landlord_id)
    reviews = Review.objects.filter(landlord_id=landlord_id)
    avg = Review.objects.filter(landlord_id=landlord_id).aggregate(a =( Avg('fixing_rate')+ Avg('liveable_cond'))/2)
    return render(request, 'reviews.html', {'reviews': reviews, 'landlord':landlord, 'avg':avg})