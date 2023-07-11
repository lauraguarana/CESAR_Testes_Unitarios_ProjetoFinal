from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self, flavor):
        """Percorra a lista de sabores disponíveis e imprima."""

        if self.flavors:
            return("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                return(f"\t-{flavor}")
        else:
            return("Estamos sem estoque atualmente!")

    def find_flavor(self, flavor):

        # ---------- BUG: correção para retornar apenas o sabor ao invés da lista completa
        # ---------- MELHORIA: removido os prints para manter o clean code

        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return(f"Sabor disponível: {flavor}!")
            else:
                return(f"Sabor não disponível: {flavor}!")
        else:
            return("Estamos sem estoque atualmente!")

    def add_flavor(self, flavor):

        # ---------- BUG: foi removida a verificação se a lista está vazia ou preenchida, pois não é necessária já que o método é para adicionar novos sabores.
        # ---------- MELHORIA: o if foi alterado para verificar se o sabor não está na lista self.flavors e adicionar o novo sabor.
        # ---------- MELHORIA: removido os prints para manter o clean code

        """Add o sabor informado ao estoque."""

        if flavor not in self.flavors:
            self.flavors.append(flavor)
            return(f"{flavor} adicionado ao estoque!")
        else:
            return("Sabor já disponível!")

    def delete_flavor(self, flavor):

        # ---------- MELHORIA: o método delete_flavor foi adicionado para caso o sabor do sorvete não esteja mais disponível no estoque.

        """Remove o sabor informado do estoque."""
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            return(f"{flavor} removido do estoque!")
        else:
            return(f"Sabor não encontrado: {flavor}!")
