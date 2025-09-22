import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validar_email(email: str) -> bool:
    """
    Verifica se a string de email fornecida corresponde ao padrão Regex.
    """
    if not email:
        return False
    
    # Versão concisa: usa bool() para garantir True/False
    return bool(EMAIL_REGEX.fullmatch(email))
