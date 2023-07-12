from unittest import TestCase
from src.restaurant import Restaurant

class TestRestaurant(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.restaurant_name = "Delicious Eatery"
        cls.cuisine_type = "Italian"
        cls.restaurant = Restaurant(cls.restaurant_name, cls.cuisine_type)

    def test_describe_restaurant(self):
        # Setup
        restaurante = Restaurant(self.restaurant_name, self.cuisine_type)
        resultado_esperado = "Restaurante: Delicious Eatery\nTipo de Cozinha: Italian\nClientes Atendidos: 0"

        # Avaliacao
        self.assertEqual(restaurante.describe_restaurant(), resultado_esperado)

    def test_open_restaurant(self):
        # Setup
        is_open = False
        resultado_esperado = f"{self.restaurant_name} agora está aberto!"

        # Avaliacao
        self.assertEqual(self.restaurant.open_restaurant(is_open=is_open), resultado_esperado)

    def test_open_restaurant_already_open(self):
        # Setup
        is_open = True
        resultado_esperado = f"{self.restaurant_name} já está aberto!"

        # Avaliacao
        self.assertEqual(self.restaurant.open_restaurant(is_open=is_open), resultado_esperado)

    def test_close_restaurant(self):
        # Setup
        is_open = True
        resultado_esperado = f"{self.restaurant_name} agora está fechado!"

        # Avaliacao
        self.assertEqual(self.restaurant.close_restaurant(is_open=is_open), resultado_esperado)

    def test_close_restaurant_already_close(self):
        # Setup
        restaurante = Restaurant(self.restaurant_name, self.cuisine_type)
        is_open = False
        resultado_esperado = f"{self.restaurant_name} está fechado!"

        # Avaliacao
        self.assertEqual(self.restaurant.close_restaurant(is_open=is_open), resultado_esperado)

    def test_set_number_served(self):
        # Setup
        is_open = True
        total_customers = 10
        resultado_esperado = "O número de pessoas atendidas foi atualizado para: " + str(total_customers)

        # Avaliacao
        self.assertEqual(self.restaurant.set_number_served(total_customers=total_customers, is_open=is_open), resultado_esperado)

    def test_set_number_served_invalid(self):
        # Setup
        is_open = True
        total_customers = -2
        resultado_esperado = "O número de clientes atendidos não pode ser negativo ou igual a zero."

        # Avaliacao
        self.assertEqual(self.restaurant.set_number_served(total_customers=total_customers, is_open=is_open), resultado_esperado)

    def test_set_number_served_closed_restaurant(self):
        # Setup
        is_open = False
        total_customers = 0
        resultado_esperado = f"{self.restaurant_name} está fechado!"

        # Avaliacao
        self.assertEqual(self.restaurant.set_number_served(total_customers=total_customers, is_open=is_open), resultado_esperado)

    def test_increment_number_served(self):
        # Setup
        more_customers = 2
        is_open = True
        updatedServed = self.restaurant.get_number_served() + more_customers
        resultado_esperado = "O número de pessoas atendidas foi atualizado para: " + str(updatedServed)

        # Avaliacao
        self.assertEqual(self.restaurant.increment_number_served(more_customers=more_customers, is_open=is_open), resultado_esperado)

    def test_increment_number_served_closed_restaurant(self):
        # Setup
        more_customers = 2
        is_open = False
        resultado_esperado = f"{self.restaurant_name} está fechado!"

        # Avaliacao
        self.assertEqual(self.restaurant.increment_number_served(more_customers=more_customers, is_open=is_open), resultado_esperado)