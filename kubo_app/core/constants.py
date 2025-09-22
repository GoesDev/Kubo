ACCOUNT_TYPE = ['Corrente', 'Poupança']

DB_FILE = 'kubo_app_database.db'

LIMITE_ALERTA_ORCAMENTO = 0.80  # 80% do orçamento consumido dispara um alerta
MOEDA_PADRAO = 'BRL'            # Código da moeda padrão (Real Brasileiro)

SQL_CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY, name TEXT NOT NULL, email_login TEXT NOT NULL, password TEXT NOT NULL)"""

SQL_INSERT_INTO_USERS = """INSERT INTO users (name, email_login, password) VALUES (?, ?, ?)"""
