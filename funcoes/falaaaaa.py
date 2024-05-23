"""
regras ae aescontos e acrescimos:

1. INSS (Instituto Nacional do Seguro Social):
. O desconto do INSS e calculado de acordo com a faixa salarial do funcionário:
· Salário até R$ 1.100,00: 7,5%
· Salário de R$ 1.100,01 até R$ 2.203,48: 9%
· Salário de R$ 2.203,49 até R$ 3.305,22: 12%
. Salário de R$ 3.305,23 até R$ 6.433,57: 14%
· O valor máximo de desconto do INSS é de R$ 854,36.

2. IRRF (Imposto de Renda Retido na Fonte):
. O desconto do IRRF é calculado de acordo com a faixa salarial do funcionário e com a
quantidade de dependentes:
· Isento: Salário até R$ 2.259,20
. 7,5%: Salario de R$ 2.259,21 até R$ 2.826,65
. 15%: Salário de R$ 2.826,66 até R$ 3.751,05
. 22,5%: Salario de R$ 3.751,06 até R$ 4.664,68
. 27,5%: Salário acima de R$ 4.664,68
· Dedução por dependente: R$ 189,59 por dependente.

3. Vale Transporte:
· Desconto de 6% do salário base do funcionário, caso opte pelo benefício.
"""