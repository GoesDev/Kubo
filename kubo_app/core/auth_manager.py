import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validar_email(email: str) -> bool:
    """
    Verifica se a string de email fornecido corresponde ao padrão
    """

    if not email:
        return False
    
    if EMAIL_REGEX.fullmatch(email):
        return True
    else:
        return False
