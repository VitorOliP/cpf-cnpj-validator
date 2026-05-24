import re
import random

def calculate_first_dv(cpf_base: str) -> int:
    """
    Calcula o primeiro dígito verificador (DV1) de um CPF.

    Args:
        cpf_base (str): Os 9 primeiros dígitos do CPF.

    Returns:
        int: Primeiro dígito verificador calculado.
    """
    nums = [int(x) for x in cpf_base]
    weights = range(10, 1, -1)
    soma = sum(n * p for n, p in zip(nums, weights))
    remainder = soma % 11
    
    return 0 if remainder < 2 else 11 - remainder

def calculate_second_dv(cpf_base: str, dv1: int) -> int:
    """
    Calcula o segundo dígito verificador (DV2) de um CPF.

    Args:
        cpf_base (str): Os 9 primeiros dígitos do CPF.
        dv1 (int): Primeiro dígito verificador já calculado.

    Returns:
        int: Segundo dígito verificador calculado.
    """
    cpf_base_dv1 = cpf_base + str(dv1)
    nums = [int(x) for x in cpf_base_dv1]    
    weights = range(11, 1, -1)
    soma = sum(n * p for n, p in zip(nums, weights))
    remainder = soma % 11
    
    return 0 if remainder < 2 else 11 - remainder
    
def generate_cpf_dv(cpf_base: str) -> str:
    """
    Gera os dois dígitos verificadores de um CPF.

    Args:
        cpf_base (str): Os 9 primeiros dígitos do CPF.

    Returns:
        str: String contendo os dois dígitos verificadores.
    """
    dv1 = calculate_first_dv(cpf_base)
    dv2 = calculate_second_dv(cpf_base, dv1)
    
    return f"{dv1}{dv2}"


def validate_cpf(cpf: str) -> bool:
    """
    Valida um CPF verificando formato, sequência repetida
    e dígitos verificadores.

    Args:
        cpf (str): CPF com ou sem caracteres de formatação.

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    # Remover caracteres não numéricos
    digits = ''.join(re.compile(r'[0-9]').findall(str(cpf)))
    
    #Verificar tamanho
    if not digits or len(digits) != 11:
        return False
    
    #Rejeitar sequências repetidas
    if digits == digits[0] * 11:
        return False
    
    cpf_base = digits[:9]
    dv = generate_cpf_dv(str(cpf_base))
    
    return digits[-2:] == dv

def generate_cpf() -> str:
    """
    Gera um CPF válido aleatório.

    Returns:
        str: CPF válido contendo 11 dígitos numéricos.
    """
    cpf_base = ''.join(str(random.randint(0, 9)) for _ in range(9))
    dv = generate_cpf_dv(cpf_base)
    
    return cpf_base + dv