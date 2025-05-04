import re

def validar_dados(nome, endereco, cpf):
    erros = []
    if not nome:
        erros.append("O nome é obrigatório.")
    if not endereco:
        erros.append("O endereço é obrigatório.")
    if not cpf:
        erros.append("O CPF é obrigatório.")
    elif not re.match(r'^\d{11}$', cpf):
        erros.append("O CPF deve conter 11 dígitos numéricos.")
    return erros