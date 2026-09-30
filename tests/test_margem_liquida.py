import pytest

from fincalc import calcular_margem_liquida


def test_margem_liquida_positiva():
    margem = calcular_margem_liquida(100000.0, 70000.0)

    assert round(margem, 2) == 30.00


def test_margem_liquida_receita_nula():
    with pytest.raises(ValueError):
        calcular_margem_liquida(0.0, 1000.0)


def test_margem_liquida_custos_negativos():
    with pytest.raises(ValueError):
        calcular_margem_liquida(10000.0, -5000.0)
