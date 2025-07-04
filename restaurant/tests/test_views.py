from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Add some test menu items
        Menu.objects.create(title="Pizza", price=12.99, inventory=10)
        Menu.objects.create(title="Burger", price=8.99, inventory=20)

    def test_get_all(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(len(menus), 2)
        self.assertEqual(serializer.data[0]["title"], "Pizza")
        self.assertEqual(serializer.data[1]["title"], "Burger")
