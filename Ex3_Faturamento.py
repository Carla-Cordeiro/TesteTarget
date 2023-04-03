# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open("dados.json") as dados_empresa:
    dado = json.load(dados_empresa)

menor_valor = float('inf')
dia = float('inf')

maior_valor = dado[0]['valor']
dia_maior = dado[0]['dia']

media = []

for faturamento in dado:
    valor_json = faturamento['valor']
    dia_json = faturamento['dia']

    if valor_json != 0:
        media.append(valor_json)
        if valor_json < menor_valor:
            menor_valor = valor_json
            dia = dia_json

    if valor_json > maior_valor:
        maior_valor = valor_json
        dia_maior = dia_json

media_final = sum(media) / len(media)

dias_maior_media = 0
for i in dado:
    if i['valor'] > media_final:
        dias_maior_media +=1


print(f'O menor valor é {menor_valor} do dia {dia}')
print(f'O maior valor é {maior_valor} do dia {dia_maior}')
print("A média é: ", media_final)
print("A quantidade de dias que o faturamento foi maior que a média, é: ", dias_maior_media)