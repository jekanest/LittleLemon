from django.test import TestCase
from models import Menu


class MenuViewTest(TestCase):
    def test_setUp(self):
        self.menuitem1 = Menu.objects.create(Title='Pasta fresca', Price='15.00', Inventory=23)
        self.menuitem2 = Menu.objects.create(Title='Tiramisu', Price='9.50', Inventory=50)
        self.menuitem3 = Menu.objects.create(Title='Pizza', Price='12.00', Inventory=4)

    def test_getall(self):
        pasta = Menu.objects.get(Title='Pasta fresca')
        tiramisu = Menu.objects.get(Title='Tiramisu')
        pizza = Menu.objects.get(Title='Salad')

        self.assertEqual(str(pasta), 'Pasta fresca : 15.00')
        self.assertEqual(str(tiramisu), 'Tiramisu : 9.50')
        self.assertEqual(str(pizza), 'Pizza : 12.00')