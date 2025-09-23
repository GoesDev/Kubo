# from core.auth_manager import validar_email
from core.constants import DB_FILE, SQL_INSERT_INTO_ACCOUNTS, SQL_DELETE_ACCOUNTS_BY_ID, SQL_SELECT_ALL_ACCOUNTS
from database.db_manager import connect_db, delete_by_id, select_all, create_table, insert_into

conexao = connect_db(DB_FILE)

# delete_by_id(conexao, SQL_DELETE_ACCOUNTS_BY_ID, '1')

# account = ('Banco pra Frentex', 'Poupanca', '200', 'Verde')

# insert_into(conexao, SQL_INSERT_INTO_ACCOUNTS, account)


# create_table(conexao, SQL_CREATE_ACCOUNTS_TABLE)


all_accounts = select_all(conexao, SQL_SELECT_ALL_ACCOUNTS)

for account in all_accounts:
    print(account)

# print(f"teste@email.com: {validar_email('teste@email.com')}")
