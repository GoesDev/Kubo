import re
import bcrypt
from core.constants import SQL_INSERT_INTO_USERS, DB_FILE
from database.db_manager import insert_into, connect_db

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

PASSWORD_REGEX = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )

def validate_email(email: str) -> bool:
    """
    Verifica se a string de email fornecida corresponde ao padrão Regex.
    """
    if not email:
        return False
    
    # Versão concisa: usa bool() para garantir True/False
    return bool(EMAIL_REGEX.fullmatch(email))

def validate_password(password: str) -> bool:
    """
    Verifica se a password atende aos requisitos de segurança.

    Args:
        password (str): A password a ser validada.

    Returns:
        bool: True se a password for válida, False caso contrário.
    """
    if not password or len(password) < 8:
        return False

    return bool(PASSWORD_REGEX.fullmatch(password))

def hash_password(password: str) -> bytes:
    """
    Criptografa a senha usando bcrypt.
    
    O bcrypt gera um 'salt' automaticamente e o inclui no hash final.
    O 'salt' é uma string aleatória que torna o hash de senhas iguais diferente,
    protegendo contra ataques de tabela arco-íris.
    
    Args:
        senha (str): A senha em texto puro.
    
    Returns:
        bytes: A senha criptografada (hash).
    """

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password

def check_password(password_to_check: str, hashed_password: bytes) -> bool:
    """
    Verifica se a senha digitada corresponde ao hash salvo.
    
    Args:
        password_to_check (str): A senha em texto puro digitada pelo usuário.
        hashed_password (bytes): O hash da senha salvo no banco de dados.
        
    Returns:
        bool: True se as senhas coincidirem, False caso contrário.
    """

    password_bytes_to_check = password_to_check.encode('utf-8')
    return bcrypt.checkpw(password_bytes_to_check, hashed_password)

def validade_new_user(name: str, email: str, password: str) -> str:
    """
    Recebe o nome, email e senha de um novo usuário, chama as funções de validação
    caso as informações sejam válidas, os dados são enviados para registro no banco

    Args:
        name (str): nome do novo usuário
        email (str): email do novo usuário, irá passar por uma validação
        password (str): senha do novo usuário, irá passar por uma validação
    """
    
    # Valida as informações de email e senha, caso ambas sejam verdadeiras
    # um novo usuário é cadastro na tabela user

    email_ok = validate_email(email)
    password_ok = validate_password(password)
    if email_ok is False:
        return "Email inválido"
    elif password_ok is False:
        return "Senha inválida"
    else:
        hashed_password = hash_password(password)

        # Cria a conexão com o banco, usando o caminho contido em DB_file
        # usa o código de insert into contido em SQL_INSERT_INTO_USERS e
        # uma tupla, fornce os dados do usuário
        insert_into(connect_db(DB_FILE), SQL_INSERT_INTO_USERS, (name, email, hashed_password))
        return "Cadastrando Novo Usuário"
