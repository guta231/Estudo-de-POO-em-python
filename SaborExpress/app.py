import requests
import json
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


url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante ={}
    for item in dados_json:
        nome_do_restaurante = item["Company"]
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })
else:
    print(response.status_code)
    
response_teste = requests.get("http://127.0.0.1:8000/api/hello")

if response_teste.status_code == 200:
    response_teste_json = response_teste.json()
    nome = response_teste_json["nome"]


def main():
    print(nome)

if __name__ == "__main__":
    main()