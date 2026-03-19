#Configurando rotas internas
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.modelos.cliente import Cliente, ClienteCriarAtualizar
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio

router = APIRouter(
    prefix='/api/clientes',
)
                                     # Serve para diferenciar e ver se é url do front ou do back
front_router = APIRouter(
    prefix='/clientes'
)

templates = Jinja2Templates(directory='templates')

'''CLIENTE_LIST = [Cliente(id_=1,nome="Rafael", email="rafael071007@gmail.com", telefone="11973630831"),  teste antes de fazer o banco de dados
                    Cliente(id_=2,nome="Lucas", email="lucasdias@gmail.com", telefone="11973665430")]'''

# Daqui para baixo sao as rotas do CRUD, onde cada uma tem uma função especifica
@router.get('/', response_model=list[Cliente]) #para retorna a estrutura do cliente, e nao uma string padrao
async def listar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()

@router.get('/{cliente_id}', response_model=Cliente | None)
async def obter_cliente(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int 
):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)

    if not cliente:
        raise HTTPException(status_code=404, detail='Cliente não encontrado')
    
    return cliente

@router.post('/', response_model=Cliente, status_code=201)
async def criar_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente: ClienteCriarAtualizar
):
    return await cliente_repositorio.criar_cliente(cliente)

@router.put('/{cliente_id}', response_model=Cliente | None)
async def atualizar_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int,
    cliente: ClienteCriarAtualizar
):
    cliente_atualizado = await cliente_repositorio.atualizar_cliente(cliente_id, cliente)
    if not cliente_atualizado:
        raise HTTPException(status_code=404, detail='Cliente não encontrado')
    
    return cliente_atualizado

@router.delete('/{cliente_id}', status_code=204)
async def deletar_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
    cliente_id: int
):
    sucesso = await cliente_repositorio.deletar_cliente(cliente_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail='Cliente não encontrado')
    
@front_router.get('/', response_class=HTMLResponse)
async def pagina_listar_clientes(request: Request, cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    clientes = await cliente_repositorio.listar_clientes()
    return templates.TemplateResponse('clientes.html', {'request': request, 'clientes': clientes, 'titulo': 'Lista de Clientes'}) #toda request do jinja precisa passar a propria request que esta sendo recebida, para ele conseguir desenhar na tela 

@front_router.get('/novo', response_class=HTMLResponse)
async def pagina_criar_cliente(request: Request):  # Toda logica esta sendo feita pelo clientes-from
    return templates.TemplateResponse('clientes-form.html', {'request': request})

@front_router.get('/{cliente_id}', response_class=HTMLResponse)
async def pagina_editar_cliente(
    request: Request,
    cliente_id: int,
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]
):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)
    return templates.TemplateResponse('clientes-form.html', {'request': request, 'cliente': cliente}
)
    