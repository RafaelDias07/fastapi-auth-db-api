from pydantic import BaseModel

# BaseModel é usado para criar um "modelo de dados" da API.
# Ele define quais campos o objeto deve ter e quais são seus tipos.
# Quando o FastAPI recebe um JSON na requisição, ele usa esse modelo
# para validar automaticamente os dados e converter o JSON em um objeto Python.
class Cliente(BaseModel):   
    id_: int   
    nome: str
    email: str
    telefone: str

class ClienteCriarAtualizar(BaseModel): # A unica diferença dessa classe para a de cima, e que nao iremos usar o id
    nome: str
    email: str
    telefone: str