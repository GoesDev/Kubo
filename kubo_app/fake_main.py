from core.auth_manager import validade_new_user, validate_login_email

resultado = validade_new_user('Usuário', 'emaul@email.com.br.net', 'P@ssw0rd')
print(resultado)

result = validate_login_email('email@email.com.br', 'P@ssw0rd')

print(result)


# for i in range(11):
#     delete_by_id(connect_db(DB_FILE), SQL_DELETE_USERS_BY_ID, str(i))

# vamo = validade_new_user('Duarda', 'email@daedra.net', 'Torr3@$s')
# print(vamo)

# print(validate_login_email('email@email.com', ''))

# conexao = connect_db(DB_FILE)

# delete_by_id(conexao, SQL_DELETE_ACCOUNTS_BY_ID, '1')


# create_table(conexao, SQL_CREATE_ACCOUNTS_TABLE)


# all_accounts = select_all(conexao, SQL_SELECT_ALL_ACCOUNTS)

# for account in all_accounts:
#     print(account)

# print(f"teste@email.com: {check_email('teste@email.com')}")
# print(f"Senha@123: {check_password('Senha@123')}")
# print(f"senhafraca: {check_password('senhafF1@raca')}")

 # 1. Hashing
# original_password = "GOES@8833a!"
# hashed_password = hash_password(original_password)

# print(f"Senha original: {original_password}")
# print(f"Senha hash (salva no DB): {hashed_password}")

# # 2. Verificação (simulando um login)
# print("\nSimulando login...")
# correct_password = "GOES@8833a!"
# incorrect_password = "SenhaIncorreta"

# # Deve ser True
# print(f"Verificando senha correta: {check_password(correct_password, hashed_password)}")
# # Deve ser False
# print(f"Verificando senha incorreta: {check_password(incorrect_password, hashed_password)}")
