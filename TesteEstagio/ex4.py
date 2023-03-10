faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
faturamento_total = sum(faturamento_estados.values())

for estado, faturamento in faturamento_estados.items():
    percentual = faturamento / faturamento_total * 100
    if estado != "Outros":
        print(f"Faturamento do estado {estado} é {percentual:.2f}%")
    else:
        print(f"Faturamento dos Outros estados é {percentual:.2f}%")
