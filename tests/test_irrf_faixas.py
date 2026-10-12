import pytest
from fincalc import calcular_irrf


@pytest.mark.parametrize(
    "salario, esperado",
    [
        (2826.65, 42.56),
        (3000.00, 68.56),
        (3751.05, 181.22),
        (5000.00, 462.23),
    ],
)
def test_irrf_faixas_superiores(salario, esperado):
    assert calcular_irrf(salario) == pytest.approx(esperado, abs=0.01)
