# 🚀 Sistema Web com FastAPI

## 📖 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação web utilizando **Python** e **FastAPI**, com foco na criação de uma API moderna, organizada e de alta performance.

A aplicação foi desenvolvida para demonstrar conceitos fundamentais do desenvolvimento backend, como criação de APIs, autenticação de usuários, operações **CRUD**, integração com banco de dados e testes automatizados.

Durante o desenvolvimento foram aplicadas boas práticas como **programação assíncrona**, **validação de dados com Pydantic**, **estrutura modular de projeto**, além da integração com **HTML, CSS, JavaScript e Jinja Templates** para a interface web.

O projeto também conta com **documentação automática da API com Swagger**, sistema de **autenticação de usuários com sessões** e **testes automatizados com PyTest**, garantindo maior organização e confiabilidade no código.

---

## ⚙️ Tecnologias Utilizadas

- **Python**
- **FastAPI**
- **SQLite**
- **Pydantic**
- **Uvicorn**
- **PyTest**
- **Jinja Templates**
- **HTML**
- **CSS**
- **JavaScript**

---

## ✨ Funcionalidades

- Criação de API utilizando **FastAPI**
- Estrutura modular para organização do projeto
- Documentação automática da API com **Swagger**
- Operações **CRUD (Create, Read, Update, Delete)**
- Integração com banco de dados **SQLite**
- Validação de dados com **Pydantic**
- Sistema de **registro de usuários**
- Sistema de **autenticação e login**
- Controle de sessão utilizando **cookies HTTP**
- Proteção de rotas utilizando **middlewares**
- Interface web com **HTML, CSS, JavaScript e Jinja**
- Testes automatizados utilizando **PyTest**

---

## 🏗 Estrutura do Projeto

```bash
project/
│
├── app/
│   ├── routers/        # Rotas da aplicação
│   ├── models/         # Modelos de dados
│   ├── repositories/   # Camada de acesso a dados
│   └── main.py         # Arquivo principal da aplicação
│
├── templates/          # Templates HTML (Jinja)
├── static/             # Arquivos CSS e JavaScript
├── tests/              # Testes automatizados
├── requirements.txt    # Dependências do projeto
└── README.md

💻 Como Utilizar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/nome-do-repositorio.git
2️⃣ Entrar na pasta do projeto
cd nome-do-repositorio
3️⃣ Criar um ambiente virtual
python -m venv venv
4️⃣ Ativar o ambiente virtual

Windows:

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate
5️⃣ Instalar as dependências
pip install -r requirements.txt
6️⃣ Executar a aplicação
uvicorn app.main:app --reload
🌐 Acessando a Aplicação

Após iniciar o servidor, acesse no navegador:

Aplicação:

http://127.0.0.1:8000

Documentação interativa da API (Swagger):

http://127.0.0.1:8000/docs
```
## 🆘 Suporte

Caso encontre algum problema ou tenha dúvidas sobre o projeto, você pode:

Abrir uma Issue neste repositório

Consultar a documentação oficial do FastAPI:

https://fastapi.tiangolo.com/

## 👨‍💻 Autor

Desenvolvido por:

Rafael Dias Fontes
