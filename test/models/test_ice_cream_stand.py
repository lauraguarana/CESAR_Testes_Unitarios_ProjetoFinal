import unittest
from src.models.restaurant import Restaurant
from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.restaurant_name = "Ice Cream Paradise"
        cls.cuisine_type = "Sorveteria"
        cls.flavors = ["Baunilha", "Chocolate", "Morango"]
        cls.ice_cream_stand = IceCreamStand(cls.restaurant_name, cls.cuisine_type, cls.flavors)

    def test_flavors_available(self, flavor):
        flavor = "Baunilha"
        sorveteria = IceCreamStand("Ice Cream Paradise", "Sorveteria", "Morango")
        resultado_esperado = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n\t-Baunilha\n\t-Chocolate\n\t-Morango\n"

        # Chamada
        resultado = sorveteria.flavors_available(flavor=flavor)

        # Avaliacao
        assert resultado_esperado == resultado


    def test_flavors_available_empty(self):
        self.ice_cream_stand.flavors = []
        resultado_esperado = "Estamos sem estoque atualmente!"
        self.assertEqual(self.ice_cream_stand.flavors_available(), resultado_esperado)

    def test_find_flavor_available(self):
        flavor = "Chocolate"
        resultado_esperado = "Sabor disponível: Chocolate!"
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), resultado_esperado)

    def test_find_flavor_not_available(self):
        flavor = "Mint"
        resultado_esperado = "Sabor não disponível: Mint!"
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), resultado_esperado)

    def test_find_flavor_empty_stock(self):
        self.ice_cream_stand.flavors = []
        resultado_esperado = "Estamos sem estoque atualmente!"
        self.assertEqual(self.ice_cream_stand.find_flavor("Vanilla"), resultado_esperado)

    def test_add_flavor_new_flavor(self):
        flavor = "Mint"
        resultado_esperado = "Mint adicionado ao estoque!"
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), resultado_esperado)

    def test_add_flavor_existing_flavor(self):
        flavor = "Vanilla"
        resultado_esperado = "Sabor já disponível!"
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), resultado_esperado)

    def test_delete_flavor_existing_flavor(self):
        flavor = "Chocolate"
        resultado_esperado = "Chocolate removido do estoque!"
        self.assertEqual(self.ice_cream_stand.delete_flavor(flavor), resultado_esperado)

    def test_delete_flavor_not_existing_flavor(self):
        flavor = "Mint"
        resultado_esperado = "Sabor não encontrado: Mint!"
        self.assertEqual(self.ice_cream_stand.delete_flavor(flavor), resultado_esperado)


if __name__ == '__main__':
    unittest.main()
