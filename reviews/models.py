from django.db import models
from django.db.models import Avg
import numpy as np


class Beer(models.Model):
    name = models.CharField(max_length=200)
    abv = models.CharField(max_length=200)
    ibu = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    ounces = models.CharField(max_length=200)

    #def average_rating(self):
        #all_ratings = map(lambda x: x.rating, self.review_set.all())
        #return np.mean(all_ratings)

    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']

    def __unicode__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    #beer_style = models.CharField(max_length=100)

#class Cluster(models.Model):
    #name = models.CharField(max_length=100)
    #users = models.ManyToManyField(User)

    #def get_members(self):
        #return "\n".join([u.username for u in self.users.all()])

# Create your models here.
