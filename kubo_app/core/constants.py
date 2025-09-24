ACCOUNT_TYPE = ['Corrente', 'Poupança']

DB_FILE = 'kubo_app_database.db'

LIMITE_ALERTA_ORCAMENTO = 0.80  # 80% do orçamento consumido dispara um alerta
MOEDA_PADRAO = 'BRL'            # Código da moeda padrão (Real Brasileiro)

#------------------------------------------------------------------------

SQL_CREATE_USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS
        users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email_login TEXT NOT NULL,
            password TEXT NOT NULL
)"""

SQL_INSERT_INTO_USERS = """
    INSERT INTO
        users (
            name,
            email_login,
            password
    ) VALUES (
        ?, ?, ?
    )
"""

SQL_SELECT_ALL_USERS = """
    SELECT
        name,
        email_login,
        password
    FROM
        users
"""

SQL_SELECT_USERS_BY_EMAIL = """
    SELECT
        name,
        password
    FROM
        users
    WHERE
        email_login = ?
"""

SQL_DELETE_USERS_BY_ID = """
    DELETE FROM
        users
    WHERE
        id = ?
"""

#------------------------------------------------------------------------

SQL_CREATE_ACCOUNTS_TABLE = """
    CREATE TABLE IF NOT EXISTS 
        accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            current_balance REAL NOT NULL,
            color TEXT NOT NULL
        )
"""

SQL_INSERT_INTO_ACCOUNTS = """
    INSERT INTO 
        accounts (
            name, 
            type, 
            current_balance, 
            color
        ) 
    VALUES (
        ?, ?, ?, ?
    )
"""

SQL_SELECT_ALL_ACCOUNTS = """
    SELECT
        name,
        type,
        current_balance,
        color
    FROM
        accounts
"""

SQL_DELETE_ACCOUNTS_BY_ID = """
    DELETE FROM
        accounts
    WHERE 
        id = ?
"""

#------------------------------------------------------------------------

SQL_CREATE_TRANSACTIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS 
        transactions (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            type TEXT CHECK (type IN ('income', 'expense', 'transfer')),
            date DATETIME NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL,
            account_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (account_id) REFERENCES accounts(id)
)"""

SQL_INSERT_INTO_TRANSACTIONS = """
    INSERT INTO transactions (
        amount,
        type,
        date, 
        description,
        user_id,
        account_id
    ) VALUES (
        ?, ?, ?, ?, ?, ?
    )
"""

SQL_SELECT_ALL_TRANSACTIONS = """
    SELECT
        name,
        type,
        current_balance,
        color
    FROM
        transactions
"""

SQL_DELETE_TRANSACTIONS_BY_ID = """
    DELETE FROM
        transactions
    WHERE 
        id = ?
"""
