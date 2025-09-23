ACCOUNT_TYPE = ['Corrente', 'Poupança']

DB_FILE = 'kubo_app_database.db'

LIMITE_ALERTA_ORCAMENTO = 0.80  # 80% do orçamento consumido dispara um alerta
MOEDA_PADRAO = 'BRL'            # Código da moeda padrão (Real Brasileiro)

#------------------------------------------------------------------------

SQL_CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY, name TEXT NOT NULL, email_login TEXT NOT NULL, password TEXT NOT NULL)"""

SQL_INSERT_INTO_USERS = """INSERT INTO users (name, email_login, password) VALUES (?, ?, ?)"""

SQL_SELECT_ALL_USERS = """SELECT name, email_login, password FROM users"""

SQL_DELETE_USERS_BY_ID = """DELETE FROM users WHERE id = ?"""

#------------------------------------------------------------------------

SQL_CREATE_ACCOUNTS_TABLE = """CREATE TABLE IF NOT EXISTS accounts (
id INTEGER PRIMARY KEY, name TEXT NOT NULL, type TEXT NOT NULL, current_balance REAL NOT NULL,
color TEXT NOT NULL)"""

SQL_INSERT_INTO_ACCOUNTS = """INSERT INTO accounts (name, type, current_balance, 
color) VALUES (?, ?, ?, ?)"""

SQL_SELECT_ALL_ACCOUNTS = """SELECT name, type, current_balance, color FROM accounts"""

SQL_DELETE_ACCOUNTS_BY_ID = """DELETE FROM accounts WHERE id = ?"""
