import pytest
from fincalc import calcular_financiamento


def test_financiamento_prestacao_padrao():
    # Arrange & Act
    tabela = calcular_financiamento(10000.0, 1.0, 12)

    # Assert
    assert len(tabela) == 12
    assert tabela[0]["prestacao"] == 888.49
    assert tabela[0]["juros"] == 100.00
    assert tabela[0]["amortizacao"] == 788.49


def test_financiamento_quita_saldo_devedor():
    # Arrange & Act
    tabela = calcular_financiamento(10000.0, 1.0, 12)

    # Assert
    assert tabela[-1]["saldo_devedor"] == 0.0


def test_financiamento_taxa_zero():
    # Arrange & Act
    tabela = calcular_financiamento(1200.0, 0.0, 12)

    # Assert
    assert tabela[0]["prestacao"] == 100.00
    assert tabela[0]["juros"] == 0.0


def test_financiamento_valor_invalido():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_financiamento(0.0, 1.0, 12)


def test_financiamento_taxa_negativa():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_financiamento(10000.0, -1.0, 12)


def test_financiamento_parcelas_invalidas():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_financiamento(10000.0, 1.0, 0)


def test_financiamento_parcelas_nao_inteiras():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_financiamento(10000.0, 1.0, 12.5)
