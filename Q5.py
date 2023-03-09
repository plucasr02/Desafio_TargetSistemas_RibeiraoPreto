#definindo a inversão
def inverter(n):
    if len(n) == 1:
        return n
    elif len(n) > 1:
        return inverter(n[1:]) + n[0]

num = input("Escreva sua string: ")
#printando a string
print(f"A string invertida é: {inverter(num)}")