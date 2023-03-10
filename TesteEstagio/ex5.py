string = input("Digite uma string: ")
reverse_string = ""

for i in range(len(string)-1, -1, -1):
    reverse_string += string[i]

print("A string invertida é:", reverse_string)
