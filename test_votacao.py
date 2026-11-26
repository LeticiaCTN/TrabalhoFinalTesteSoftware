
from votacao import verificar_situacao_eleitoral


def test_menor_de_16_anos():
    assert verificar_situacao_eleitoral(15) == "Não pode votar"


def test_voto_facultativo():
    assert verificar_situacao_eleitoral(17) == "Voto facultativo"


def test_voto_obrigatorio():
    assert verificar_situacao_eleitoral(30) == "Voto obrigatório"


def test_maior_de_70_anos():
    assert verificar_situacao_eleitoral(75) == "Voto facultativo"


def test_idade_invalida():
    assert verificar_situacao_eleitoral(-1) == "Idade inválida"
