class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):

        # -------- ERRO DE DIGITAÇÃO: foi corrigido o nome "restaurante" que estava errado.
        # -------- MELHORIA: De acordo com o Clean Code, a descrição do restaurante foi atualizada pelo código abaixo.
        # -------- Anteriormente, na chamada do nome do restaurante estava sendo utilizado o self.cuisine_type ao invés do self.restaurant_name

        """Imprima uma descrição simples da instância do restaurante."""
        description = f"Restaurante: {self.restaurant_name}\nTipo de Cozinha: {self.cuisine_type}\nClientes Atendidos: {self.number_served}"

        return description

    def open_restaurant(self, is_open):

        # ---------- BUG: a atribuição self.number_served = -2 estava incorreta. Isso definirá o número de clientes atendidos como -2 quando o restaurante for aberto.
        # ---------- Foi adicionado um parametro indicando se o restaurante está aberto ou fechado.

        """Imprime uma mensagem indicando que o restaurante está aberto para negócios."""
        if is_open:
            print(f"{self.restaurant_name} já está aberto!")
        else:
            self.open = True
            print(f"{self.restaurant_name} agora está aberto!")

    def close_restaurant(self, is_open):

        # ---------- BUG: foi removido o self.number_served = 0 porque o número de clientes atendidos não precisa ser resetado quando o restaurante é fechado.
        # ---------- Foi adicionado um parametro indicando se o restaurante está aberto ou fechado.

        """Imprime uma mensagem indicando que o restaurante está fechado para negócios."""
        if is_open:
            self.open = False
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers, is_open):

        # ---------- MELHORIA: foi adicionado uma validação para que o número de pessoas atendidas seja maior ou igual a zero.
        # ---------- Foi adicionado uma mensagem para informando que o número de pessoas atendidas foi atualizado
        # ---------- Foi adicionado um parametro indicando se o restaurante está aberto ou fechado.

        """Define o número total de pessoas atendidas por este restaurante até o momento."""
        if is_open:
            if total_customers >= 0:
                self.number_served = total_customers
                print(f"O número de pessoas atendidas foi atualizado para: {total_customers}")
            else:
                print("O número de clientes atendidos não pode ser negativo.")
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers, is_open):

        # ---------- BUG: self.number_served = more_customers para self.number_served += more_customers para incrementar o número total de clientes atendidos.
        # ---------- MELHORIA: foi adicionado uma validação para que o novo número de pessoas atendidas seja maior que zero.
        # ---------- Foi adicionado uma mensagem para informando que o número de pessoas atendidas foi atualizado
        # ---------- Foi adicionado um parametro indicando se o restaurante está aberto ou fechado.

        """Aumenta o número total de clientes atendidos por este restaurante."""
        if is_open:
            if more_customers > 0:
                self.number_served += more_customers
                print(f"O número de pessoas atendidas foi atualizado para: {self.number_served}")
        else:
            print(f"{self.restaurant_name} está fechado!")

    def get_number_served(self):

        # -------- MELHORIA: foi adicionado esse método para  obter o número total de clientes atendidos até o momento.

        """Retorna o número total de clientes atendidos até o momento."""
        return self.number_served