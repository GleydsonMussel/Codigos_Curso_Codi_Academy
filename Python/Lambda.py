import random

# Funções lambda seguem uma declaração enxuta: variavel = lambda input: comportamento

funcao_com_input = lambda x:x*2 if x%2==0 else x*3

funcao_sem_input = lambda : print("Aoba")

print(funcao_com_input(2))
print(funcao_com_input(3))

funcao_sem_input()

# EXERCÍCIO: Crie uma lista de números e ordene-a de forma crescente usando uma função lambda.
lista = []
[lista.append(random.randint(0, 100)) for i in range(10)]

print(lista)

ordenador = lambda lista: lista.sort()

ordenador(lista)
print(lista)