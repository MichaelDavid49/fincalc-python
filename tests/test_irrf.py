import pytest
from fincalc import calcular_irrf


def test_irrf_faixa_dois():
    # Arrange & Act
    imposto = calcular_irrf(2500.00)
    # Assert
    assert round(imposto, 2) == 18.06


def test_irrf_limite_isencao():
    # Arrange & Act
    imposto = calcular_irrf(2259.20)
    # Assert
    assert round(imposto, 2) == 0.0


def test_irrf_salario_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_irrf(-1000.00)
