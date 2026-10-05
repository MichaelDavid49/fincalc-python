# fincalc-python

Aplicação financeira simples para testes do grupo 3.

## Parte 2 — Aluno 3

Foi implementado o cálculo de financiamento e amortização pelo sistema
Tabela Price na função `calcular_financiamento`, disponível em
`fincalc.py`.

A função recebe:

- valor financiado;
- taxa de juros mensal, em porcentagem;
- número de parcelas.

O retorno é a tabela completa do financiamento, contendo o número da parcela,
a prestação fixa, os juros, a amortização e o saldo devedor.

### Exemplo

```python
tabela = calcular_financiamento(10000.0, 1.0, 12)

for parcela in tabela:
    print(parcela)
```

Para um financiamento de R$ 10.000,00, à taxa de 1% ao mês, dividido em
12 parcelas, a prestação fixa calculada é de R$ 888,49.

### Resolução de conflito no README

Na resolução de conflitos deste arquivo, o conteúdo original do projeto deve
ser preservado junto às novas informações de cada integrante. Os marcadores
`<<<<<<<`, `=======` e `>>>>>>>` devem ser removidos após a escolha ou
combinação do conteúdo correto, antes do commit de resolução.
