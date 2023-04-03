# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
from time import sleep

faturamento = {
    'São Paulo': 67836.43,
    'Rio de Janeiro': 36678.66,
    'Minas Gerais': 29229.88,
    'Espírito Santo': 27165.4,
    'Outros': 19849.53
}

total = sum(faturamento.values())

for key, valor in faturamento.items():
    #  print(f'Estado: {key}, Valor: {valor}')

    porcentagem = valor / total * 100
    print(f'Estado: {key} - Percentual: {porcentagem:.4f}%')
    sleep(1)
