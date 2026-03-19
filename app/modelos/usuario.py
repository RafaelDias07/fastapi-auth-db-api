from pydantic import BaseModel

# BaseModel é usado para criar um "modelo de dados" da API.
# Ele define quais campos o objeto deve ter e quais são seus tipos.
# Quando o FastAPI recebe um JSON na requisição, ele usa esse modelo
# para validar automaticamente os dados e converter o JSON em um objeto Python.
class Usuario(BaseModel):   
    id_: int   
    nome: str
    email: str
    senha: str | None = None

class UsuarioCriarAtualizar(BaseModel):
    nome: str
    email: str
    senha: str | None = None