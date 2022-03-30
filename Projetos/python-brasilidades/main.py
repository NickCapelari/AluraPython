from acesso_cep import BuscaEndereco

cep = 86181900

objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf, logradouro = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf, logradouro)