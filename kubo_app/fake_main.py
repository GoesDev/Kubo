# from core.auth_manager import validar_email
from core.constants import DB_FILE, SQL_DELETE_USERS_BY_ID, SQL_SELECT_ALL_USERS
from database.db_manager import connect_db, delete_by_id, select_all

conexao = connect_db(DB_FILE)

# delete_by_id(conexao, SQL_DELETE_USERS_BY_ID, '3')

# user = ('Kassandra', 'rata@kassandra.com', '777')

# insert_into(conexao, SQL_INSERT_INTO_USERS, user)


# create_table(conexao, SQL_CREATE_USERS_TABLE)


# all_users = select_all(conexao, SQL_SELECT_ALL_USERS)

# for user in all_users:
#     print(user)

# print(f"teste@email.com: {validar_email('teste@email.com')}")
