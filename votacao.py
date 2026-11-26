
def verificar_situacao_eleitoral(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade < 16:
        return "Não pode votar"
    elif idade < 18:
        return "Voto facultativo"
    elif idade <= 70:
        return "Voto obrigatório"
    else:
        return "Voto facultativo"
