from fastapi import FastAPI, Query
import requests

app = FastAPI()

teste = {
    "nome":"gustavo"
}
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)

@app.get("/api/hello")
def hello_world():
    return teste


@app.get("/api/restaurantes/")
def cardapio_restaurante(restaurante: str = Query(None)):
    
    if response.status_code == 200:
        dados_json = response.json()
        dados_restaurante = []
        for item in dados_json:
            if restaurante == item["Company"]:
                dados_restaurante.append({
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"]
                })
        return {restaurante: dados_restaurante}
    else:
        return {"Erro": response.status_code}