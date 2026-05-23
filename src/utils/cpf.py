import re
import random

def calcular_dv1(cpf_base: str) -> int:
    nums = [int(x) for x in cpf_base]
    pesos = range(10, 1, -1)
    soma = sum(n * p for n, p in zip(nums, pesos))
    resto = soma % 11
    
    return 0 if resto < 2 else 11 - resto

def calcular_dv2(cpf_base: str, dv1: int) -> int:
    cpf_base_dv1 = cpf_base + str(dv1)
    nums = [int(x) for x in cpf_base_dv1]    
    pesos = range(11, 1, -1)
    soma = sum(n * p for n, p in zip(nums, pesos))
    resto = soma % 11
    
    return 0 if resto < 2 else 11 - resto
    
def gerar_digitos_cpf(cpf_base: str) -> str:
    dv1 = calcular_dv1(cpf_base)
    dv2 = calcular_dv2(cpf_base, dv1)
    
    return f"{dv1}{dv2}"


def validar_cpf(cpf: str) -> bool:
    # Remover caracteres não numéricos
    digits = ''.join(re.compile(r'[0-9]').findall(str(cpf)))
    
    #Verificar tamanho
    if not digits or len(digits) != 11:
        return False
    
    #Rejeitar sequências repetidas
    if digits == digits[0] * 11:
        return False
    
    cpf_base = digits[:9]
    dv = gerar_digitos_cpf(str(cpf_base))
    
    return digits[-2:] == dv

def gerar_cpf() -> str:
    cpf_base = ''.join(str(random.randint(0, 9)) for _ in range(9))
    dv = gerar_digitos_cpf(cpf_base)
    
    return cpf_base + dv