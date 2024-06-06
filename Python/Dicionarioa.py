dicionario = {"chave1":"valor1"}

# Para adicionar chaves, basta salvar um valor em um chave que até então não existia
dicionario["chave2"] = 12

# Para deletar uma chave, .pop("chave")
dicionario.pop("chave2")

# É possível comparar de forma direta se determinada chave existe no dicionario
print("chave2" in dicionario)
