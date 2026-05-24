import re
import random
import string


def calculate_first_dv(cnpj_base: str) -> int:
    """
    Calcula o primeiro dígito verificador (DV1) de um CNPJ.

    O cálculo utiliza os 12 caracteres base do CNPJ (numérico ou
    alfanumérico), convertendo cada caractere para seu valor ASCII
    ajustado conforme a regra oficial do CNPJ alfanumérico.

    Args:
        cnpj_base (str): Os 12 caracteres iniciais do CNPJ.

    Returns:
        int: Primeiro dígito verificador calculado.
    """
    nums = [ord(x) - 48 for x in cnpj_base]
    weights = list(range(5, 1, -1)) + list(range(9, 1, -1))
    soma = sum(n * p for n, p in zip(nums, weights))
    remainder = soma % 11
    return 0 if remainder < 2 else 11 - remainder


def calculate_second_dv(cnpj_base: str, dv1: int) -> int:
    """
    Calcula o segundo dígito verificador (DV2) de um CNPJ.

    Utiliza os 12 caracteres base juntamente com o primeiro dígito
    verificador para determinar o segundo dígito conforme a regra
    oficial de validação do CNPJ.

    Args:
        cnpj_base (str): Os 12 caracteres iniciais do CNPJ.
        dv1 (int): Primeiro dígito verificador já calculado.

    Returns:
        int: Segundo dígito verificador calculado.
    """
    nums = [ord(x) - 48 for x in cnpj_base] + [dv1]
    weights = list(range(6, 1, -1)) + list(range(9, 1, -1))
    soma = sum(n * p for n, p in zip(nums, weights))
    remainder = soma % 11
    return 0 if remainder < 2 else 11 - remainder


def generate_cnpj_dv(cnpj_base: str) -> str:
    """
    Gera os dois dígitos verificadores de um CNPJ.

    Args:
        cnpj_base (str): Os 12 caracteres iniciais do CNPJ.

    Returns:
        str: String contendo os dois dígitos verificadores.
    """
    dv1 = calculate_first_dv(cnpj_base)
    dv2 = calculate_second_dv(cnpj_base, dv1)
    return f"{dv1}{dv2}"


def validate_cnpj(cnpj: str) -> bool:
    """
    Valida um CNPJ numérico ou alfanumérico.

    A validação remove caracteres inválidos, verifica o tamanho,
    rejeita sequências compostas por um único caractere repetido
    e compara os dígitos verificadores informados com os calculados.

    Args:
        cnpj (str): CNPJ com ou sem caracteres de formatação.

    Returns:
        bool: True se o CNPJ for válido, False caso contrário.
    """
    chars = ''.join(re.compile(r'[A-Z0-9]').findall(str(cnpj).upper()))

    if not chars or len(chars) != 14:
        return False

    if chars == chars[0] * 14:
        return False

    cnpj_alfanum_base = chars[:12]

    # NÃO converter para string numérica
    dv = generate_cnpj_dv(cnpj_alfanum_base)

    return chars[-2:] == dv


def generate_cnpj_base() -> str:
    """
    Gera a parte base de um CNPJ numérico.

    Returns:
        str: Sequência aleatória de 12 dígitos numéricos.
    """
    return ''.join(str(random.randint(0, 9)) for _ in range(12))


def generate_cnpj() -> str:
    """
    Gera um CNPJ numérico válido.

    Returns:
        str: CNPJ válido contendo 14 caracteres numéricos.
    """
    cnpj_base = generate_cnpj_base()
    dv = generate_cnpj_dv(cnpj_base)
    return cnpj_base + dv


def generate_cnpj_alfanum_base() -> str:
    """
    Gera a parte base de um CNPJ alfanumérico.

    Os caracteres podem ser letras maiúsculas (A-Z) ou dígitos (0-9).

    Returns:
        str: Sequência aleatória de 12 caracteres alfanuméricos.
    """
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(12))


def generate_cnpj_alfanum() -> str:
    """
    Gera um CNPJ alfanumérico válido.

    Returns:
        str: CNPJ alfanumérico válido contendo 14 caracteres.
    """
    cnpj_alfanum_base = generate_cnpj_alfanum_base()
    dv = generate_cnpj_dv(cnpj_alfanum_base)
    return cnpj_alfanum_base + dv

def format_cnpj(cnpj: str) -> str:
    return (
        f"{cnpj[:2]}."
        f"{cnpj[2:5]}."
        f"{cnpj[5:8]}/"
        f"{cnpj[8:12]}-"
        f"{cnpj[12:]}"
    )
    
def format_cnpj_alfanum(cnpj: str) -> str:
    return (
        f"{cnpj[:2]}."
        f"{cnpj[2:5]}."
        f"{cnpj[5:8]}/"
        f"{cnpj[8:12]}-"
        f"{cnpj[12:]}"
    )