import re
import random
import string


def calcular_dv1(cnpj_base: str) -> int:
    nums = [ord(x) - 48 for x in cnpj_base]
    pesos = list(range(5, 1, -1)) + list(range(9, 1, -1))
    soma = sum(n * p for n, p in zip(nums, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def calcular_dv2(cnpj_base: str, dv1: int) -> int:
    nums = [ord(x) - 48 for x in cnpj_base] + [dv1]
    pesos = list(range(6, 1, -1)) + list(range(9, 1, -1))
    soma = sum(n * p for n, p in zip(nums, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def gerar_digitos_cnpj(cnpj_base: str) -> str:
    dv1 = calcular_dv1(cnpj_base)
    dv2 = calcular_dv2(cnpj_base, dv1)
    return f"{dv1}{dv2}"


def validar_cnpj(cnpj: str) -> bool:
    chars = ''.join(re.compile(r'[A-Z0-9]').findall(str(cnpj).upper()))

    if not chars or len(chars) != 14:
        return False

    if chars == chars[0] * 14:
        return False

    cnpj_alfanum_base = chars[:12]

    # NÃO converter para string numérica
    dv = gerar_digitos_cnpj(cnpj_alfanum_base)

    return chars[-2:] == dv


def gerar_cnpj_base() -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(12))


def gerar_cnpj() -> str:
    cnpj_base = gerar_cnpj_base()
    dv = gerar_digitos_cnpj(cnpj_base)
    return cnpj_base + dv


def gerar_cnpj_alfanum_base() -> str:
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(12))


def gerar_cnpj_alfanum() -> str:
    cnpj_alfanum_base = gerar_cnpj_alfanum_base()
    dv = gerar_digitos_cnpj(cnpj_alfanum_base)
    return cnpj_alfanum_base + dv