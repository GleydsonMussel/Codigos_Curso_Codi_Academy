# Tuplas são imutáveis, mas é possível fazer a mesma variável armazenar outra tupla
tupla = ("Elemento 1", 2)
tupla_2 = (1 , 2, 3.0)

# Para acessar elementos é igual lista/vetor

# É possível, semmelhante a Sets, verificar se a tupla armazena um item em específico de forma direta
esta = 2 in tupla

print(esta)

tupla = tupla.__add__(tupla_2)

print(tupla)