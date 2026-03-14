from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.rotas import cliente, login, registro
from app.autenticação_middleware import AuthenticationToken

templates = Jinja2Templates(directory='templates')


app = FastAPI(
    title='Techlog Solutions API',
    description='CRM para Techlog Solutions',
    version='1.0.0',
)

app.mount('/static', StaticFiles(directory='static'), name='static') #qualquer arquivo que voce colocar aqui dentro ele vai navega, dentro de da pasta static
app.add_middleware(AuthenticationToken)

app.include_router(cliente.router) #adicionando uma nova rota, pegando a rota do cliente para o fastapi conseguir ler
app.include_router(cliente.front_router)

app.include_router(login.router)
app.include_router(registro.router)

@app.get('/health')
async def health_check():
    return{'status': 'OK'} # Se por acaso isso nao retornar, sabemos que nosso servidor nao esta mais de pé

@app.get('/', response_class=HTMLResponse)
async def front_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'titulo': 'TechLog Solutions CRM', 'versao': '1.0.0'})

@app.get('/logout')
async def logout():
    response = RedirectResponse(url='/login', status_code=303)
    response.delete_cookie('session_token')
    return response 


