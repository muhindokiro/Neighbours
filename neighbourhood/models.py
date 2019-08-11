from django.contrib.auth.models import User
from django.db import models
import datetime as dt

# Create y models here.
class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    image = models.ImageField(upload_to='images/', blank=True)
    occupants = models.IntegerField()

    @classmethod
    def home(cls):
        neighbourhood = cls.objects.filter()
        return neighbourhood

    @classmethod
    def search_by_neighbourhood_name(cls,search_term):
        neighbourhood = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbourhood
    
        
    @classmethod
    def get_neighbourhood_by_id(cls,id):
        neighbourhood = cls.objects.get(pk=id)
        return neighbourhood

class Post(models.Model):
    post = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    profession = models.CharField(max_length =60)
    status = models.CharField(max_length =60)
    contact = models.IntegerField()
    neighbourhood = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile/', blank=True)

    @classmethod
    def profile(cls):
        profile = cls.objects.filter()
        return profile

    def save_profile(self):
        self.save()


