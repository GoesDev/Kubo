import sqlite3, os
from core.constants import DB_FILE, SQL_CREATE_USERS_TABLE, SQL_INSERT_INTO_USERS

def connect_db(db_file):

    conn = None

    try:
        conn = sqlite3.connect(db_file)
    
    except sqlite3.Error as e:
        print(f'Error: {e}')
    
    return conn

def create_table(conn, sql):

    if conn is not None:

        try:

            cursor = conn.cursor()

            cursor.execute(sql)

            conn.commit()
        
        except sqlite3.Error as e:
            print(f'Error: {e}')
    
    else:
        print('There is not a db connection!')

def insert_into(conn, sql, data):

    cursor = conn.cursor()
    cursor.execute(sql, data)

    conn.commit()

    return cursor.lastrowid

conexao = connect_db(DB_FILE)

if conexao:
    pass
    # create_table(conexao, SQL_CREATE_USERS_TABLE)
    # user = ('Duarda', 'duarda.@gmail.com', '664hh')
    # user_1 = insert_into(conexao, SQL_INSERT_INTO_USERS, user)
    # print(user_1)
