#Lista 3 - Exercício 6

a = int(input('Informe um número inteiro: '))
b = int(input('Informe um número inteiro: '))
c = int(input('Informe um número inteiro: '))
if a > b and a > c:
    if b > c:
        print(f'A ordem crescente é: {c, b, a}')
    else:
        print(f'A ordem crescente é: {b, c, a}')
elif b > a and b > c:
    if a > c:
        print(f'A ordem crescente é: {c, a, b}')
    else:
        print(f'A ordem crescente é: {a, c, b}')
else:
    if a > b:
        print(f'A ordem crescente é: {b, a, c}')
    else:
        print(f'A ordem crescente é: {a, b, c}')
