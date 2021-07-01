from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_itemname_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_donefield_is_not_required(self):
        form = ItemForm({'name': 'Test', 'done': ''})
        self.assertTrue(form.is_valid())

    def test_field_are_explicit_in_formmetaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields,  ['name', 'done'])