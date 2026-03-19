import sqlite3
from contextlib import contextmanager  # é um decorator, ele garante que o codigo faz a conexao

class BancoDeDadosLocal():
    def __init__(self, nome_arquivo='techlog.db'):  #função para iniciar o banco de dados
        self.nome_arquivo = nome_arquivo
        self.inicializar_banco()

   
    @contextmanager
    def conectar(self):
        conexao = sqlite3.connect(self.nome_arquivo)
        try:
            yield conexao
            conexao.commit()
        except Exception as e:
            conexao.rollback()
            raise e 
        finally:
            conexao.close()   # Aqui simplesmente funciona como, pediu/usamos, depois que pediu ele ja fecha, garantido que nao vms gastar coisas a mais

    def inicializar_banco(self):
        with self.conectar() as conexao:
            cursor = conexao.cursor()   # Criando a tabela clientes no banco caso, ela nao exista, depois cria um id com primary key, todos usarios vao ter nome, email e telefone
            cursor.execute( '''
                CREATE TABLE IF NOT EXISTS clientes (  
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL         
                )
            ''')
            cursor.execute( '''
                CREATE TABLE IF NOT EXISTS usuarios (  
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL         
                )
            ''')
            conexao.commit()
            
          

