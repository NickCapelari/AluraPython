url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
#sanitização da URL
url = url.strip()

#validação da URL
if url == "":
    raise ValueError("URL vazia")
else:
    #Separa a base e os parametros
    indice_interrogacao = url.find('?')
    url_base = url[:indice_interrogacao]
    url_parametros = url[indice_interrogacao+1:]
    print(url_parametros)
    #busca o valor de um parametro
    parametro_busca = "moedaOrigem"
    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    if indice_e_comercial == -1:
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)