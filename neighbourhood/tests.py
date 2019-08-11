from django.test import TestCase
from .models import NeighbourHood,Post,Profile

# Create your tests here.
class NeighbourHoodTestClass(TestCase):

    def setUp(self):
        self.new_neighbourhood= NeighbourHood(title = 'Test neighbourhood',neighbourhood = 'This is a random test NeighbourHood')
        self.new_neighbourhood.save()

    def tearDown(self):
        NeighbourHood.objects.all().delete()

class PostTestClass(TestCase):

    def setUp(self):
        self.new_post= Post(title = 'Test post',post = 'This is a random test post')
        self.new_post.save()

    def tearDown(self):
        Post.objects.all().delete()

class ProfileTestClass(TestCase):

    def setUp(self):
        self.new_profile= Profile(title = 'Test profile',profile = 'This is a random test Profile')
        self.new_profile.save()


    def tearDown(self):
        Profile.objects.all().delete()