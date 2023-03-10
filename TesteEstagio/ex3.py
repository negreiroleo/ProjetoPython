import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

menor_valor_com_faturamento = None
menor_valor = None
maior_valor = None
soma_faturamento = 0
dias_faturamento = 0
for dados_dia in dados:
    valor = dados_dia["valor"]
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor
    if (menor_valor_com_faturamento is None or valor < menor_valor_com_faturamento) and valor:
        menor_valor_com_faturamento = valor
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
    if valor:
        soma_faturamento += valor
        dias_faturamento += 1

media_faturamento = soma_faturamento / dias_faturamento

dias_faturamento_media = [x["dia"] for x in dados if x["valor"] >= media_faturamento]

#Não foi específicado ignorar os dias sem faturamento no cálculo de menor faturamento, os dias de menor faturamento serão 0
print(f"O menor faturamento em um dia no mês foi: {menor_valor}")
print(f"O menor faturamento em um dia no mês com faturamento foi: {menor_valor_com_faturamento}")
print(f"O maior faturamento em um dia no mês foi: {maior_valor}")
print(f"A média diária de faturamento no mês foi: {media_faturamento}")
print(f"Quantidade de dias em que o faturamento foi maior que a média diária do mês: {len(dias_faturamento_media)}")