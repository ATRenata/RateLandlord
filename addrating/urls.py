from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('show/<int:landlord_id>', views.show_reviews, name='show_rev'),
    path('<int:landlord_id>', views.addreview, name='review'),
]
