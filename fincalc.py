# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros compostos."""
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_aposentadoria(
    patrimonio_atual: float,
    aporte_mensal: float,
    anos: int,
    taxa_anual: float,
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_rendimento_real(ganho_nominal: float, inflacao: float) -> float:
    """Calcula a taxa de retorno real descontada a inflação do período."""
    retorno_real = (
        (1 + (ganho_nominal / 100)) / (1 + (inflacao / 100))
    ) - 1
    return retorno_real * 100


def calcular_margem_liquida(receita_total: float, custos_totais: float) -> float:
    """Calcula a margem de lucro líquida percentual de uma operação."""
    lucro = receita_total - custos_totais
    return (lucro / receita_total) * 100


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    # Teste de Juros Simples
    montante_s = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante_s:.2f}")

    # Teste de Juros Compostos
    montante_c = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_c:.2f}")

    # Teste de Aposentadoria
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")

    # Teste de IRRF (Aluno 2 - Wanderson)
    salario_teste = 3000.0
    irrf = calcular_irrf(salario_teste)
    print(f"IRRF (Salário R$ {salario_teste:.2f}): R$ {irrf:.2f}")

    # Teste de Rendimento Real
    rendimento_real = calcular_rendimento_real(10.0, 4.0)
    print(f"Rendimento Real (ganho de 10% e inflação de 4%): {rendimento_real:.2f}%")

    # Teste de Margem Líquida (Aluno 7- Julia )
    margem = calcular_margem_liquida(10000.0, 7000.0)
    print(f"Margem Líquida (Receita R$ 10.000, Custos R$ 7.000): {margem:.2f}%")
