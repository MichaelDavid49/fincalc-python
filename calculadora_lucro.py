from pathlib import Path

code = '''# ============================================
# CÁLCULO DE LUCRO E MARGENS
# Trabalho de Faculdade - Python
# ============================================

print("======================================")
print("     CALCULADORA DE LUCRO EMPRESARIAL")
print("======================================")

receita = float(input("Digite a receita total da empresa: R$ "))
custos = float(input("Digite o total de custos: R$ "))
despesas_operacionais = float(input("Digite as despesas operacionais: R$ "))
impostos = float(input("Digite o valor dos impostos: R$ "))

lucro_bruto = receita - custos

lucro_operacional = lucro_bruto - despesas_operacionais

lucro_liquido = lucro_operacional - impostos

if receita != 0:
    margem_operacional = (lucro_operacional / receita) * 100
    margem_liquida = (lucro_liquido / receita) * 100
else:
    margem_operacional = 0
    margem_liquida = 0

# Exibição dos resultados
print("\\n======================================")
print("             RESULTADOS")
print("======================================")

print(f"Receita total: R$ {receita:,.2f}")
print(f"Lucro bruto: R$ {lucro_bruto:,.2f}")
print(f"Lucro operacional: R$ {lucro_operacional:,.2f}")
print(f"Lucro líquido: R$ {lucro_liquido:,.2f}")
print(f"Margem operacional: {margem_operacional:.2f}%")
print(f"Margem de lucro líquido: {margem_liquida:.2f}%")

print("======================================")
'''

readme = '''# Calculadora de Lucro Empresarial

Projeto desenvolvido em Python para um trabalho de faculdade.


O programa recebe os seguintes dados:

- Receita total
- Custos
- Despesas operacionais
- Impostos

A partir desses valores, calcula:

- Lucro bruto
- Lucro operacional
- Lucro líquido
- Margem operacional
- Margem de lucro líquido

```bash
python calculadora_lucro.py
