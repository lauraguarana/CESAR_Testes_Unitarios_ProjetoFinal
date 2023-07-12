from unittest import TestCase
from src.ice_cream_stand import IceCreamStand

class TestIceCreamStand(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.flavors = ["Baunilha", "Chocolate", "Morango"]
        cls.ice_cream_stand = IceCreamStand(cls.flavors)

    def test_flavors_available(self):
        # Setup
        iceCream = IceCreamStand(["Baunilha", "Chocolate", "Morango"])
        resultado_esperado = ["Baunilha", "Chocolate", "Morango"]

        print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
        print(iceCream.flavors_available())

        # Avaliacao
        self.assertEqual(iceCream.flavors_available(), resultado_esperado)

    def test_flavors_available_empty(self):
        # Setup
        self.ice_cream_stand.flavors = []
        resultado_esperado = "Estamos sem estoque atualmente!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.flavors_available(), resultado_esperado)

    def test_find_flavor_available(self):
        # Setup
        flavor = "Morango"
        resultado_esperado = "Sabor disponível: " + flavor + "!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), resultado_esperado)

    def test_find_flavor_not_available(self):
        # Setup
        iceCream = IceCreamStand(["Baunilha", "Chocolate", "Morango"])
        flavor = "Mint"
        resultado_esperado = "Sabor não disponível: " + flavor + "!"

        # Avaliacao
        self.assertEqual(iceCream.find_flavor(flavor), resultado_esperado)

    def test_find_flavor_empty_stock(self):
        # Setup
        self.ice_cream_stand.flavors = []
        flavor = "Baunilha"
        resultado_esperado = "Estamos sem estoque atualmente!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), resultado_esperado)

    def test_add_flavor_new_flavor(self):
        # Setup
        flavor = "Flocos"
        resultado_esperado = flavor + " adicionado ao estoque!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), resultado_esperado)

    def test_add_flavor_existing_flavor(self):
        # Setup
        flavor = "Baunilha"
        resultado_esperado = "Sabor já disponível!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), resultado_esperado)

    def test_delete_flavor_existing_flavor(self):
        # Setup
        flavor = "Flocos"
        resultado_esperado = flavor + " removido do estoque!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.delete_flavor(flavor), resultado_esperado)

    def test_delete_flavor_not_existing_flavor(self):
        # Setup
        flavor = "Mint"
        resultado_esperado = "Sabor não encontrado: " + flavor + "!"

        # Avaliacao
        self.assertEqual(self.ice_cream_stand.delete_flavor(flavor), resultado_esperado)

