# É possível em um for each também pegar o índice no qual aquele elemento se encontra dentro da estrutura, basta usar o enumerate
lista = [1, 2, 3, 4]

for indice, elemento in enumerate(lista):
    print(indice)
    print(elemento)