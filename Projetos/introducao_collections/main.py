def proximo_ano(idade):
    return idade+1


idades = [39, 30, 27, 18]
idades.append(15)
print(idades)
idades.remove(30)
print(idades)
print(27 in idades)
idades.insert(3,10)
print(idades)
idades.extend([50,85])
print(idades)

idades_ano_que_vem = [(idade+1) for idade in idades]
print(idades_ano_que_vem)

print([(idade) for idade in idades if idade < 21])

print([proximo_ano(idade) for idade in idades if idade > 21])

idades.clear()
print(idades)

