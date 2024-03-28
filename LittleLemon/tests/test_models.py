from django.test import TestCase
from models import Menu


class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(ttle='Gelato', Price=7.50, Inventory=50)
        self.assertEqual(str(item), "Gelato : 7.50")