import pytest
from fincalc import calcular_juros_simples


def test_juros_simples_valido():
    assert round(calcular_juros_simples(1000.0, 5.0, 2), 2) == 1100.00


def test_juros_simples_tempo_zero():
    assert round(calcular_juros_simples(1000.0, 5.0, 0), 2) == 1000.00


def test_juros_simples_capital_negativo():
    with pytest.raises(ValueError):
        calcular_juros_simples(-500.0, 5.0, 2)


def test_juros_simples_tempo_negativo():
    with pytest.raises(ValueError):
        calcular_juros_simples(1000.0, 5.0, -1)
