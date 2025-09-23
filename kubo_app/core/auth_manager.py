import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

PASSWORD_REGEX = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )

def check_email(email: str) -> bool:
    """
    Verifica se a string de email fornecida corresponde ao padrão Regex.
    """
    if not email:
        return False
    
    # Versão concisa: usa bool() para garantir True/False
    return bool(EMAIL_REGEX.fullmatch(email))

def check_password(password: str) -> bool:
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