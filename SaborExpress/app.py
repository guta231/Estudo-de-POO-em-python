from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante("Praça", "Gourmet")
bebida_suco = Bebida("suco de melancia", 5.00, "Grande")
prato_paozinho = Prato("paozinho", 2.00, "O melhor paozinho")
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
sobremesa_pudim = Sobremesa("Pudim", 10.00, "De leite", "Médio", "Pudim de leite bem docinho")
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)

def main():
    restaurante_praca.listar_cardapio

if __name__ == "__main__":
    main()