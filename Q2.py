# Checa se é fibonacci
def e_fibonacci(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        a = 0
        b = 1
        while b < n:
            c = a + b
            a = b
            b = c
        return b == n

num = int(input("Digite um número: "))

#Condição se é ou não fibonacci
if e_fibonacci(num):
    # Printar fibonacci até o número
    print(f"Sequência de Fibonacci até {num}: ")
    a = 0
    b = 1
    print(a)
    while b <= num:
        print(b)
        c = a + b
        a = b
        b = c
    print("-----------------------------------------")
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")