import pytest
from fincalc import calcular_aposentadoria


def test_aposentadoria_valida():
    resultado = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    assert round(resultado, 2) == 265277.59


def test_aposentadoria_tempo_zero():
    assert calcular_aposentadoria(10000.0, 500.0, 0, 6.0) == 10000.0


def test_aposentadoria_aporte_negativo():
    with pytest.raises(ValueError):
        calcular_aposentadoria(10000.0, -500.0, 20, 6.0)


def test_aposentadoria_anos_negativos():
    with pytest.raises(ValueError):
        calcular_aposentadoria(10000.0, 500.0, -1, 6.0)
