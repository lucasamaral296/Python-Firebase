# Criar o projeto no Firebase

# Criar o Database (atenção as regras de segurança)

# Estrutura da árvore

# Interação com o Database (REST API)

import requests
import json 

# criando um arquivo para armazenar o link do database
from dbfirebase import linkdb


# Criar uma venda (POST)

# dados = {'Cliente': 'Estefany', 'Preco': 150, 'Produto': 'Teclado'}
# requisicao = requests.post(f'{linkdb}/Vendas/.json', data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Criar um novo produto (POST)

# dados = {'Nome': 'Teclado', 'Preco': 150, 'Quantidade': '10'}
# requisicao = requests.post(f'{linkdb}/Produtos/.json', data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Edtar a venda (PATCH)

# dados = {'Cliente': 'Jorge'}
# requisicao = requests.patch(f'{linkdb}/Vendas/-Na9UnucdRt9ntN3Wtfq/.json', data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Pegar uma venda especifica ou todas as vendas (GET)

requisicao = requests.get(f"{linkdb}/Vendas/.json")
print(requisicao)
dic_requisicao = requisicao.json()
id_estefany = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['Cliente']
    if cliente == "Estefany":
        id_estefany = id_venda
        print(id_venda)
        
# Deletar uma venda (DELETE)

requisicao = requests.delete(f'{linkdb}/Vendas/{id_estefany}/.json')
print(requisicao)
print(requisicao.text)

# O que seria de legal após isso?

# Autenticação

