from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test ToDo Item')
        created_item = Item.objects.get(id=item.id)
        self.assertFalse(created_item.done)
        
