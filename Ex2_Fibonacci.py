# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

num = int(input("Informe um número que deseja descobrir se faz parte da Sequência de Fibonacci: "))

ultimo = 0
penultimo = 1

fibo = []

while True:
    resultado = ultimo + penultimo
    penultimo = ultimo
    ultimo = resultado

    fibo.append(resultado)

    if num == resultado:
        print(f'O número informado ({num}) FAZ parte da sequência Fibonacci')
        print(f'Fibonacci {fibo}')
        break
    elif resultado > num:
        print(f'O número informado ({num}) NÃO FAZ parte da sequência Fibonacci')
        print(f'Fibonacci {fibo}')
        break
