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
        is_open = False
        restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = "Delicious Eatery agora está aberto!"

        # Chamada
        resultado = restaurante.open_restaurant(is_open=is_open)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_open_restaurant_already_open(self):
        is_open = True
        restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = "Delicious Eatery já está aberto!"

        # Chamada
        resultado = restaurante.open_restaurant(is_open=is_open)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_close_restaurant(self):
        is_open = True
        restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = "Delicious Eatery agora está fechado!"

        # Chamada
        resultado = restaurante.close_restaurant(is_open=is_open)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_close_restaurant_already_close(self):
        is_open = False
        restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = "Delicious Eatery já está fechado!"

        # Chamada
        resultado = restaurante.close_restaurant(is_open=is_open)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_set_number_served(self):
        is_open = True
        total_customers = 10
        #restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = (f"O número de pessoas atendidas foi atualizado para: {total_customers}")

        # Chamada
        resultado = self.restaurant.set_number_served(is_open, total_customers)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_set_number_served_close_restaurant(self):
        total_customers = 100
        is_open = False
        restaurante = Restaurant("Delicious Eatery", "Italian")
        resultado_esperado = "Delicious Eatery está fechado!"

        # Chamada
        resultado = restaurante.set_number_served(is_open, total_customers)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_increment_number_served(self):
        assert False
