from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthenticationToken(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_path = request.url.path

        # Rotas públicas devem ser acessíveis sem autenticação.
        # Isso é essencial para que assets do front-end (ex: /static/css/style.css)
        # sejam carregados na primeira renderização (antes do usuário logar).
        public_prefixes = (
            "/login",
            "/registro",   # (projeto atual)
            "/register",   # (tolerância caso exista rota homônima)
            "/static",     # assets CSS/JS
            "/docs",       # Swagger UI
            "/redoc",      # ReDoc (se estiver habilitado)
        )
        public_exact_paths = {
            "/openapi.json",
        }
        if request_path.startswith(public_prefixes) or request_path in public_exact_paths:
            return await call_next(request)
        
        token = request.cookies.get('session_token')

        if token != 'token-senha':
            return RedirectResponse(url='/login', status_code=303)
        
        return await call_next(request)