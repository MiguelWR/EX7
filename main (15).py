#Exercício 7

def impar(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 1:
        return 2 * impar(n - 1) + 1
    else:
        return 2 * impar(n - 1)

print(impar(7))