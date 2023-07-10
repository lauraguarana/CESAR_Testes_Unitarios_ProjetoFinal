from unittest import TestCase
from src.models.restaurant import Restaurant

class TestRestaurant(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.restaurant_name = "Delicious Eatery"
        cls.cuisine_type = "Italian"
        cls.restaurant = Restaurant(cls.restaurant_name, cls.cuisine_type)

    def test_describe_restaurant(self): # PASSED
        #SETUP
        resultado_esperado = "Restaurante: Delicious Eatery\nTipo de Cozinha: Italian\nClientes Atendidos: 0"

        #AVALIAÇÃO
        self.assertEqual(self.restaurant.describe_restaurant(), resultado_esperado)

    def test_open_restaurant(self):
        is_open = True
        restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = "Delicious Eatery já está aberto!"

        # Chamada
        resultado = restaurante.open_restaurant(is_open=is_open)
        print(resultado)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_close_restaurant(self):
        assert False

    def test_set_number_served(self):
        assert False

    def test_increment_number_served(self):
        assert False
