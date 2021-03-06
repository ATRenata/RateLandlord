from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm

# Create your models here.
from landlord.models import Landlord

RATING = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]
BINARY = [
    (False, 'No'),
    (True, 'Yes')
]
class Review(models.Model):

    fixing_rate = models.IntegerField(choices=RATING)
    liveable_cond = models.IntegerField(choices=RATING)
    review = models.TextField(max_length=1000, null=False)
    take_again = models.BooleanField(choices=BINARY)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, null=True)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['fixing_rate', 'liveable_cond', 'take_again','review', 'landlord']
