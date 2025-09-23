import re
import bcrypt

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
