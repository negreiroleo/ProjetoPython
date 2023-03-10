# define o número de termos que queremos gerar na sequência
num_termos = 10

# inicializa os primeiros dois termos da sequência
termo1 = 0
termo2 = 1

# imprime os primeiros dois termos da sequência
print(termo1)
print(termo2)

# gera os próximos termos da sequência e os imprime
for i in range(2, num_termos):
    proximo_termo = termo1 + termo2
    print(proximo_termo)
    termo1 = termo2
    termo2 = proximo_termo
