import sqlite3, os
from core.constants import DB_FILE, SQL_CREATE_USERS_TABLE, SQL_INSERT_INTO_USERS

def connect_db(db_file: str):
    """
    Cria e retorna a conexão com o banco de dados SQLite.

    Se o arquivo do banco de dados não existir, ele é criado. 
    Se houver um erro na conexão, imprime o erro e retorna None.

    Args:
        db_file (str): O caminho completo para o arquivo .db.

    Returns:
        sqlite3.Connection or None: Objeto de conexão com o banco de dados,
                                    ou None se a conexão falhar.
    """
    conn = None

    try:
        # Tenta conectar ao arquivo. Se não existir, o SQLite o cria.
        conn = sqlite3.connect(db_file)
    
    except sqlite3.Error as e:
        # Captura e exibe o erro em caso de falha de conexão (ex: permissões)
        print(f'Error: {e}')
    
    return conn

def create_table(conn, sql: str):
    """
    Cria uma nova tabela no banco de dados caso ela não exista.

    Args:
        conn (sqlite3.Connection): Objeto de conexão com o banco de dados

        sql (str): string com o código SQL a ser executado.
    """
    if conn is not None:
        # Verifica se existe uma conexão com o banco de dados
        try:
            # Se houver, é criado um cursor e é executado o código no SQLite
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        
        except sqlite3.Error as e:
            # Captura e exibe um erro em caso de falha na criação da tabela
            print(f'Error: {e}')
    
    else:
        # Se não houver conexão, imprime na tela uma mensagem de aviso
        print('There is not a db connection!')

def insert_into(conn, sql: str, data: tuple):
    """
    Insere novos dados ao banco de dados. A tabela alvo e as informações
    depende das variáveis fornecidas em sql e data

    Args:
        conn (sqlite3.Connection): Objeto de conexão com o banco de dados

        sql (str): string com o código SQL a ser executado.

        data (tuple): tupla com os dados a serem inseridos.
    """

    # Cria um cursor através da conexão com o banco de dados, e em seguida
    # executa o código SQL inserindo novos dados ao banco.
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()

conexao = connect_db(DB_FILE)

if conexao:
    pass
    # create_table(conexao, SQL_CREATE_USERS_TABLE)
    # user = ('Duarda', 'duarda.@gmail.com', '664hh')
    # user_1 = insert_into(conexao, SQL_INSERT_INTO_USERS, user)
