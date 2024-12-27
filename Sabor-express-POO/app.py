from restaurante import Restaurante



restaurante_praca = Restaurante("Praça", "Gourmet")

restaurante_praca.receber_avaliacao("Pedro", 10)
restaurante_praca.receber_avaliacao("Gustavo", 8)
restaurante_praca.receber_avaliacao("joão", 5)




def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()